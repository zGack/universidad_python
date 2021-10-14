try:
    archivo = open('test.txt', 'w')
    archivo.write('Agregamos informacion al archivo\n')
    archivo.write('Adiós')
except Exception as e:
    print(e)
finally:
    archivo.close()
