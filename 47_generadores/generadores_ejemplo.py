# Generador de numeros del 1 al 5
def gen_numeros():
    for numero in range(1, 6):
        yield numero
        print('Se reanuda la ejecucion de la funcion')

gen = gen_numeros()
print(f'Obj generador ')