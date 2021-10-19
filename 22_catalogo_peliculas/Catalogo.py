from Pelicula import Pelicula
import os

class Catalogo:
    ruta_archivo = 'peliculas.txt'
    
    @classmethod
    def agregar_pelicula(cls, pelicula):
        with open(cls.ruta_archivo, 'a', encoding='utf8') as archivo:
            archivo.write(f'{pelicula.pelicula}\n')
        
    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo, 'r', encoding='utf8') as archivo:
            print('CATALOGO DE PELICULAS'.center(50,'='))
            print(archivo.read())

    def eliminar(cls):
        os.remove(cls.ruta_archivo)
        print('Archivo Eliminado')
            