# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Пример:
# - Для n = 6:
#     [2.0, 2.25, 2.3704, 2.4414, 2.4883, 2.5216]
#     Сумма чисел = 14.0717


def get_sum(num):
    sum = 0
    for i in range(1, num + 1):
        sum += (1 + 1 / i)**i
    return round(sum, 4)


number = int(input('Введите число: '))
print(f'{number} => {get_sum(number)}')