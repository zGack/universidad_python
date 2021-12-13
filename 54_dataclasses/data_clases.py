from dataclasses import dataclass
from typing import ClassVar

@dataclass(eq=True, frozen=True)
class Domicilio:
    calle: str
    numero: int = 0

@dataclass(eq=True, frozen=True)
class Persona:
    nombre: str
    apellido: str
    domicilio: Domicilio
    contador_personas: ClassVar[int] = 0

    def __post_init__(self):
        if not self.nombre:
            raise ValueError(f'Valore de nombre vacio: {self.nombre}')

if __name__ == '__main__':
    domicilio1 = Domicilio('El castillo', 12)
    persona1 = Persona('Sebas', 'Mena', domicilio1)
    print(persona1)

    # Variable de clase
    print(f'Variable clase: {Persona.contador_personas}')

    # Variable de instancia
    print(f'Variables de instancia: {persona1.__dict__}')
    
    # Variable con valores vacios
    #persona_vacia = Persona('', '')
    #print(f'Persona vacia: {persona_vacia}')

    # Revisar igualdad entre objetos
    persona2 = Persona('Sebas', 'Mena', domicilio1)
    print(f'Objs iguales?: {persona1 == persona2}')

    # Agregar esta clase a una coleccion
    # (frozen=True)
    # collection = {persona1, persona2}