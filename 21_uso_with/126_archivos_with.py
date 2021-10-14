from ManejoArchivo import ManejoRecursos

#with open('test.txt', 'r', enconding='utf8') as archivo:

with ManejoRecursos('test.txt') as archivo:
    print(archivo.read())
