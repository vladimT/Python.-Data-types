error = 'ошибка, следуйте ранее указанным условиям ввода'
numbers = input('Введите числа через пробел: ')
user_number = int(input('Введите любое число: '))
def is_int(str):
    str = str.replace(' ', '')
    try:
        int(str)
        return True
    except ValueError:
        return False



if " " not in numbers:
    numbers = input('\nВведите несколько целых чисел через пробел: ')
if not is_int(numbers):
    print('\nНекорректный ввод\n')
    print(error)
else:
    numbers = numbers.split()

list_numbers = [int(item) for item in numbers]

def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result

list_numbers = merge_sort(list_numbers)

def binary_search(array, element, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        return 'Введите число в рамках диапазона'

print(f'Отсортированный по возрастанию список: {list_numbers}')

if not binary_search(list_numbers, user_number, 0, len(list_numbers)):
    rI = min(list_numbers, key=lambda x: (abs(x - user_number), x))
    ind = list_numbers.index(rI)
    max_ind = ind + 1
    min_ind = ind - 1
    if rI < user_number:
        print(f'''В списке нет введенного числа 
Ближайшее меньшее число: {rI}, индекс: {ind}
Ближайшее большее число: {list_numbers[max_ind]} индекс: {max_ind}''')
    elif min_ind < 0:
        print(f'''В списке нет введенного числа
Ближайшее большее число: {rI}, с индексом: {list_numbers.index(rI)}
В списке нет меньшего числа''')
    elif rI > user_number:
        print(f'''В списке нет введенного числа
Ближайшее большее число: {rI}, с индексом: {list_numbers.index(rI)}
Ближайшее меньшее: {list_numbers[min_ind]} с индексом: {min_ind}''')
    elif list_numbers.index(rI) == 0:
        print(f'Индекс введенного числа: {list_numbers.index(rI)}')
else:
    print(f'Индекс введенного числа: {binary_search(list_numbers, user_number, 0, len(list_numbers))}')