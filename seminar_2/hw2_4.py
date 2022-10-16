# Задать список из N элементов, заполненных числами из [-N, N].
# Найти произведение элементов на указанных позициях.
# Позиции хранятся в списке positions - создайте этот список (например: positions = [1, 3, 6])


def get_list(num):
    list = []
    for i in range(-num, num + 1):
        list.append(i)
    return list


def multiply_items(list_numbers, positions):
    multiply = 1
    for i in positions:
        multiply *= list_numbers[i]
    return multiply


number = int(input('Введите число: '))
positions = [1, 3, 6]
list_numbers = get_list(number)
print(f'{list_numbers} => {positions} => {multiply_items(list_numbers, positions)}')