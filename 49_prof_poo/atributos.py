class Persona:
    contador_personas = 0

    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido

# Mostrar los atributos de un objeto
persona1 = Persona('Sebas', 'Mena')
print(persona1.__dict__)

# Crear un atributo al vuelo
persona1.contador_personas = 10

print(persona1.__dict__)

# Accediendo al atributo de clase
print(Persona.contador_personas)

# Creando un segundo objeto
persona2 = Persona('Valen', 'Lozada')
print(persona2.__dict__)
print(persona2.contador_personas)
