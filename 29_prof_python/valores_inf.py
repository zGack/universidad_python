# Manejo de valores infinitos
import math
from decimal import Decimal

inf_p = float('INF')
# print(f'Infinito negativo {inf_n}')
# print(f'Es infinito: {math.isinf(inf_p)}')


inf_n = float('-INF')
# print(f'Infinito negativo {inf_n}')
# print(f'Es infinito: {math.isinf(inf_p)}')

# MODULO MATH
inf_p = math.inf
# print(f'Infinito postivo {inf_p}')
# print(f'Es infinito: {math.isinf(inf_p)}')

inf_n = -math.inf
# print(f'Infinito negativo {inf_n}')
# print(f'Es infinito: {math.isinf(inf_n)}')

# MODULO DECIMAL
inf_p = Decimal('Infinity')
# print(f'Infinito postivo {inf_p}')
# print(f'Es infinito: {math.isinf(inf_p)}')

inf_n = Decimal('-Infinity')
print(f'Infinito negativo {inf_n}')
print(f'Es infinito: {math.isinf(inf_n)}')

