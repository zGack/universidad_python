from Conexion import *
from Persona import Persona
from CursorPool import CursorPool

class PersonaDAO:
    '''
    DAO ( DATA ACCESS OBJECT )
    CRUD ( CREATE READ UPDATE DELETE )
    '''
    _SELECT = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERT = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    _UPDATE = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
    _DELETE = 'DELETE FROM persona WHERE id_persona = %s'

    @classmethod
    def select(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()

            personas = []

            for reg in registros:
                persona = Persona(reg[0], reg[1], reg[2], reg[3])
                personas.append(persona)

            return personas

    @classmethod
    def insert(cls, persona):
        with CursorPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email)
            cursor.execute(cls._INSERT, valores)

            log.debug(f'Persona insertada: {persona}')
            return cursor.rowcount

    @classmethod
    def update(cls, persona):
        with CursorPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
            cursor.execute(cls._UPDATE, valores)

            log.debug(f'Persona actualizada: {persona}')
            return cursor.rowcount

    @classmethod
    def delete(cls, persona):
        with CursorPool() as cursor:
            valores = (persona.id_persona,)
            cursor.execute(cls._DELETE, valores)

            log.debug(f'Persona eliminada: {persona}')
            return cursor.rowcount



if __name__ == '__main__':
    # INSERT PERSONA
    # persona1 = Persona(nombre='Manolo', apellido='Mena', email='mmena@gmail.com')
    # personas_inserts = PersonaDAO.insert(persona1)
    # log.debug(f'Personas insertadas: {personas_inserts}')

    # UPDATE PERSONA
    persona1 = Persona(1, 'Sebas', 'Mena', 'smf-mena@hotmail.com')
    personas_update = PersonaDAO.update(persona1)
    log.debug(f'Persona actualizadas: {personas_update}')

    # DELETE PERSONA
    # persona1 = Persona(id_persona = 13)
    # personas_delete = PersonaDAO.delete(persona1)
    # log.debug(f'Personas eliminadas: {personas_delete}')


    # SELECT OBJECTS
    personas = PersonaDAO.select()
    for pers in personas:
        log.debug(pers)
