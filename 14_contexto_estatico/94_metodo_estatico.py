class MiClase:
    variable_clase = 'Valor variable clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    @staticmethod
    def metodo_estatico():
        MiClase.variable_clase += ' modificado'

MiClase.metodo_estatico()
print(MiClase.variable_clase) 
