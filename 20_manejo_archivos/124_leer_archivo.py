try:
    #archivo = open('/home/sebastian/Documentos/cursos/universidad_python/20_manejo_archivos/test.txt', 'r')
    archivo = open('test.txt', 'r')
    #print(archivo.read())

    # leer algunos caracteres
    # print(archivo.read(5))

    # leer lineas completas
    # print(archivo.readline())

    # iterar el archivo
    # for line in archivo:
    #     print(line)

    # leer lineas
    # print(archivo.readlines())

    # acceder a una linea de la lista
    # print(archivo.readlines()[1])

    # abrimos un nuevo archivo
    # a - anexar informadion
    archivo2 = open('copia.txt', 'a', encoding='utf8')
    archivo2.write(archivo.read())

except Exception as e:
    print(e)
finally:
    archivo.close()
    archivo2.close()
