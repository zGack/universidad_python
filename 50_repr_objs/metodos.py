# Representacion de objetos (srt, repr, format)
# print(dir(object))

class Persona:
    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido

    # repr, mas enfocado a los programadores
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(nombre:{self.nombre}, apellido:{self.apellido})'

    # str, es mas para el usuario final u otros sistemas
    def __str__(self) -> str:
        return f'{self.__class__.__name__}: {self.nombre} {self.apellido}'

    # format, se llama por defecto cuando se usa f-string
    def __format__(self, __format_spec) -> str:
        return f'{self.__class__.__name__} con nombre {self.nombre} y apellido {self.apellido}'

persona1 = Persona('Sebas', 'Mena')

# REPR
print(f'Mi objeto: {persona1!r}')

# STR
print(f'Mi objeto: {persona1.__str__()}')

# FORMAT
print(f'{persona1}')