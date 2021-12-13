# Bool contiene los valores de True y False
# Tipos numericos, 0 para False y True para los demas valores

valor = 0
resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')

valor = 15
resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')

# Tipo str, False para '' True para los demas valores
valor = ''
resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')

valor = 'valelo'
resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')

# Tipo colecciones, False para colecciones vacias, True para todas las demas colecciones
valor = []
resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')

valor = [1]
resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')

# Tupla
valor = ()
resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')

valor = (1)
resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')

# Tupla
valor = {}
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')

valor = {"1":10}
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')