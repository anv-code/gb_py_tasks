# 2. Орел и решка


def get_count(text):
    count = 0
    tmp = 0
    for i in text:
        if i == 'Р':
            count += 1
            if count > tmp:
                tmp = count
        else:
            count = 0
    return count


text = 'OOOРОРОРОРРРРООРРРРРРР'
print(f'Последовательность: {text}')
print(f'Максимальная последовательность решки: {get_count(text)}')
