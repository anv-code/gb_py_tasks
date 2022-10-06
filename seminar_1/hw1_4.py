# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y)


def get_coordinates(num):
    if num == 1 or num == '1':
        return 'x > 0 и y > 0'
    elif num == 2 or num == '2':
        return 'x < 0 и y > 0'
    elif num == 3 or num == '3':
        return 'x < 0 и y < 0'
    elif num == 4 or num == '4':
        return 'x > 0 и y < 0'
    else:
        return 'Такой четверти не существует'


number = int(input('Введите номер четверти: '))
print(get_coordinates(number))