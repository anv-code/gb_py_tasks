# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


lst = [1, 2, 3, 15, 21, 17, 3, 2, 1]


def get_unique_numbers(lst):
    result_lst = []

    for i in lst:
        if lst.count(i) == 1:
            result_lst.append(i)
    return result_lst


print(f'{lst} -> {get_unique_numbers(lst)}')