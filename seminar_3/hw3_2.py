# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]


list = [2, 3, 4, 5, 6]
list2 = [2, 3, 5, 6]


def multiply_couple(list):
    res_list = []
    x = len(list) - 1
    for i in range(0, len(list)):
        res_list.append(list[i] * list[x])
        x -= 1
        if (x <= i):
            break
    return res_list


print(f'{list} -> {multiply_couple(list)}')
print(f'{list2} -> {multiply_couple(list2)}')