# NaN - Not a Number
# NaN es un tipo de dato numerico indefinido
import math
from decimal import Decimal

a = float('NaN')
# print(f'{a}')
# print(f'Es NaN? {math.isnan(a)}')

a = Decimal('NaN')
print(f'{a}')
print(f'Es NaN? {math.isnan(a)}')