# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

def check_predicat(one, two, three):
    return not(one or two or three) == (not one and not two and not three)

def print_result(predicat):
    result = check_predicat(predicat[0], predicat[1], predicat[2])
    print(f'{predicat[0]}, {predicat[1]}, {predicat[2]} -> {result}')


print_result([0, 0, 0])
print_result([0, 0, 1])
print_result([0, 1, 0])
print_result([0, 1, 1])
print_result([1, 0, 0])
print_result([1, 0, 1])
print_result([1, 1, 0])
print_result([1, 1, 1])