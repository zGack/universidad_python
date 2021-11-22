from Usuario import *
from UsuarioDAO import UsuarioDAO

if __name__ == '__main__':
    opt = 0

    while opt != 5:
        print(f'\n\n1) Listar usuarios')
        print(f'2) Agregar usuario')
        print(f'3) Actualizar usuario')
        print(f'4) Eliminar usuario')
        print(f'5) Salir')

        try:
            opt = int(input("> "))

        except ValueError as v_e:
            print(f'Debe ingresar una opcion valida [1 - 5]')

        except Exception as e:
            print(f'Se presento un error, intente nuevamente')

        else:
            if (opt == 1):
                usuarios = UsuarioDAO.select()
                for user in usuarios:
                    print(user)

            elif (opt == 2):
                usern = input("Digite un nombre de usuario: ")
                passw = input("Digite un password: ")

                user = Usuario(username = usern, password=passw)

                UsuarioDAO.insert(user)
                print(f'Usuario agregado correctamente')

            elif (opt == 3):
                _id = int(input("Digite el id del usuario: "))
                n_usern = input("Digite el nuevo nombre de usuario: ")
                n_passw = input("Digite la nueva contraseña: ")

                user = Usuario(_id, n_usern, n_passw)

                UsuarioDAO.update(user)
                print(f'Usuario actualizado correctamente')

            elif (opt == 4):
                _id = int(input("Digite el id del usuario: "))

                user = Usuario(id = _id)

                UsuarioDAO.delete(user)
                print(f'Usuario eliminado correctamente')

            else:
                opt = 5


