resultado = None


try:
    a = int(input("Primer numero: "))
    b = int(input("Segundo numero: "))
    resultado = a / b
except ZeroDivisionError as z_e:
    print(f'ZeroDivisionError un error: {z_e}, {type(z_e)}')
except TypeError as t_e:
    print(f'TypeError {t_e}, {type(t_e)}')
except Exception as e:
    print(f'Exception {e}, {type(e)}')

print(f'Resultado: {resultado}')
print('Continuamos...')
