# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11


def get_sum(num):
    sum = 0
    for i in num:
        if i != ',' and i != '.':
            sum += int(i)
    return sum


number = input('Введите число: ')
dig_sum = get_sum(number)
print(f'{number} -> {dig_sum}')