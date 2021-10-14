from clasePersona import Persona

def __main__():
    print("Creacion objetos".center(30,'-'))
    person1 = Persona('Sebas', 'Mena', 22)
    person1.mostrar_detalle()

    print("Eliminacion objetos".center(30,'-'))
    del person1

__main__()
