from Conexion import *
from Usuario import Usuario
from CursorPool import CursorPool

class UsuarioDAO:
    '''
    DAO ( DATA ACCESS OBJECT )
    CRUD ( CREATE READ UPDATE DELETE )
    '''
    _SELECT = 'SELECT * FROM usuarios ORDER BY id'
    _INSERT = 'INSERT INTO usuarios(username, password) VALUES(%s, %s)'
    _UPDATE = 'UPDATE usuarios SET username = %s, password = %s WHERE id = %s'
    _DELETE = 'DELETE FROM usuarios WHERE id = %s'

    @classmethod
    def select(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()

            usuarios = []

            for reg in registros:
                usuario = Usuario(reg[0], reg[1], reg[2])
                usuarios.append(usuario)

            return usuarios

    @classmethod
    def insert(cls, usuario):
        with CursorPool() as cursor:
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERT, valores)

            log.debug(f'Usuario insertado: {usuario}')
            return cursor.rowcount

    @classmethod
    def update(cls, usuario):
        with CursorPool() as cursor:
            valores = (usuario.username, usuario.password, usuario.id)
            cursor.execute(cls._UPDATE, valores)

            log.debug(f'Usuario actualizado: {usuario}')
            return cursor.rowcount

    @classmethod
    def delete(cls, usuario):
        with CursorPool() as cursor:
            valores = (usuario.id,)
            cursor.execute(cls._DELETE, valores)

            log.debug(f'Usuario eliminado: {usuario}')
            return cursor.rowcount



if __name__ == '__main__':
    # INSERT PERSONA
    # user1 = Usuario(username='Valelo', password='v321')
    # users_inserts = UsuarioDAO.insert(user1)
    # log.debug(f'Usuarios insertados: {users_inserts}')

    # UPDATE PERSONA
    user1 = Usuario(2, 'Sebas', 's123')
    user_update = UsuarioDAO.update(user1)
    log.debug(f'Usuario actualizadas: {user_update}')

    # DELETE PERSONA
    user1 = Usuario(id = 3)
    users_delete = UsuarioDAO.delete(user1)
    log.debug(f'Usuarios elimindos: {users_delete}')


    # SELECT OBJECTS
    personas = UsuarioDAO.select()
    for pers in personas:
        log.debug(pers)
