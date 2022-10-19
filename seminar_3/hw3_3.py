# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19


list = [1.1, 1.2, 3.1, 5, 10.01]


def diff_max_min(list):
    min = 0
    max = 0
    for i in list:
        num = i % 1
        if num > max:
            max = num
        elif num < min:
            min = num
    res = max - min
    return res


print(f'{list} = > {diff_max_min(list)}')