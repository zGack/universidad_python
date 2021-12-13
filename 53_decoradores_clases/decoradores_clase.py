import inspect

# Decoradores de Clase
def decorador_repr(cls):
    print('Se ejecuta decorador')
    print(f'Recibimos el objeto de la clase: {cls.__name__}')

    # Se revisan los attrs de la clase con el metodo vars
    attr = vars(cls)
    # for nombre, atributo in attr.items():
        # print(nombre, atributo)

    # Se revisan si se ha sobreescrito el metodo __init__
    if '__init__' not in attr:
        raise TypeError(f'{cls.__name__} no ha sobreescrito el metodo __init__')

    firma_init = inspect.signature(cls.__init__)
    # print(f'Firma de metodo __init__: {firma_init}')

    # Se recuperan los parametros, excepto self
    param_init = list(firma_init.parameters)[1:]
    # print(f'Parametros __init__: {param_init}')
    
    # Se revisa si por cada parametro tiene un metodo property asociado
    for param in param_init:
        # property es un valor de tipo built-in para preguntar si
        # se esta utilizando el decorador propery
        es_metodo_property = isinstance(attr.get(param), property)
        if not es_metodo_property:
            raise TypeError(f'No existe un metodo property para el parametro: {param}')

    # Se crea el metodo repr dinamicamente
    def metodo_repr(self):
        # Se obtiene el nombre de la clase dinamicamente
        nombre_cls = self.__class__.__name__
        # print(f'Nombre de la clase: {nombre_cls}')

        # Se obtiene el nombre de las propiedades dinamicamente
        # Expresion generadora, crear nombre_attr = valor_attr
        generador_args = (f'{nombre} = {getattr(self, nombre)!r}' for nombre in param_init)
        # Lista de args
        lista_arg = list(generador_args)
        # print(f'Lista del generador: {lista_arg}')
        
        # Se crea la cadena a partir de la lista de args
        args = ', '.join(lista_arg)
        # print(f'Agumentos del metodo repr: {args}')

        # Se crea la forma del metodo __repr__, sin el nombre
        resultado_metedo_repr = f'{nombre_cls}({args})'
        # print(f'Resultado del metodo repr: {resultado_metedo_repr}')

        return resultado_metedo_repr

    # Se agrega dinamicamente el metodo repr a la clase
    setattr(cls, '__repr__', metodo_repr)

    return cls

@decorador_repr
class Persona:
    def __init__(self, nombre, apellido, edad) -> None:
        print('Se ejecuta el inicializador')
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        
    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def edad(self):
        return self._edad

    # def __repr__(self):
    #   return f'Persona({self._nombre} {self._apellido})

if __name__ == '__main__':
    persona1 = Persona('Valen', 'Lozada', '21')
    print(persona1) 