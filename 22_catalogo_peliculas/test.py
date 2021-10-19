from Pelicula import Pelicula
from Catalogo import Catalogo

if __name__ == '__main__':
    catalogo = Catalogo()
    opt = 0

    while opt != 4:
        try:
            print('')
            print('MENU'.center(50,'-'))
            print('1) Agregar una pelicula')
            print('2) Mostar peliculas')
            print('3) Eliminar archivo de peliculas')
            print('4) Salir')

            opt = int(input('\n> '))
        except Exception as e:
            print(f'\nOcurrio un error: {e}')
            opt = 0

        if opt == 1:
            nombre_p = str(input('Digite el nombre de la pelicula: '))
            pelicula = Pelicula(nombre_p)
            catalogo.agregar_pelicula(pelicula)
        
        elif opt == 2:
            catalogo.listar_peliculas()
        
        elif opt == 3:
            catalogo.eliminar()

        elif opt != 0:
            opt = 4            
