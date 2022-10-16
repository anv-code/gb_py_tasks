# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def get_list(num):
    list = []
    multiply = 1
    for i in range(1, num + 1):
        multiply *= i
        list.append(multiply)
    return list


number = int(input('Введите число: '))
dig_list = get_list(number)
print(f'{number} -> {dig_list}')