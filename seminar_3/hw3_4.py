# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# 45 -> 101101
# 3 -> 11
# 2 -> 10


def get_binary_num(num):
    res = ''
    while num != 0:
        res = str(num % 2) + res
        num //= 2
    return res


number = int(input('Введите число: '))
print(f'{number} -> {get_binary_num(number)}')

