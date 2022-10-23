# Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141.$ $10^{-1} ≤ d ≤10^{-10}$
import math


def get_pi(d):
    dig = 0

    while d < 1:
        d *= 10
        dig += 1
    return round(math.pi, dig)


number = float(input('Введите точность числа: '))
print(f'π = {get_pi(number)}')