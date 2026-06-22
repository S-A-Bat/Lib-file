def sum_negative_between_min_max(arr):
    if len(arr) < 2:
        return 0

    min_idx = arr.index(min(arr))
    max_idx = arr.index(max(arr))
    start = min(min_idx, max_idx)
    end = max(min_idx, max_idx)

    total = 0
    for i in range(start + 1, end):
        if arr[i] < 0:
            total += arr[i]
    return total


# Ввод размера массива
try:
    N = int(input("Введите размер массива N: "))
except ValueError:
    print("Ошибка: введите целое число!")
    exit()

# Проверка на маленький размер
if N < 3:
    print(f"Ошибка: для вычисления суммы между min и max нужно хотя бы 3 элемента, а Вы ввели {N}.")
    print("Попробуйте снова с размером массива  N ≥ 3.")
else:
    A = list(map(int, input(f"Введите {N} элемента(ов) массива через пробел: ").split()))

    if len(A) != N:
        print("Ошибка: количество введённых элементов не соответствует N!")
    else:
        result = sum_negative_between_min_max(A)
        print(f"Сумма отрицательных элементов между минимальным и максимальным: {result}")