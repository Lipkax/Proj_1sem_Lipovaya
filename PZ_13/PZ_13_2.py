# В матрице найти максимальный положительный элемент, кратный 4.
from random import randint

len_m = int(input('Введите размер матрицы: '))  # ввод размер матрицы

m = [[randint(-20, 20) for _ in range(len_m)] for _ in range(len_m)]  # создание матрицы
for row in m:
    print(*row)
print()


def find_four(a):  # нахождение максимально положительного элемента кратного 4
    try:
        arr = max(a, key=max)
        print(max(x for x in arr if x > 0 and x % 4 == 0))
    except ValueError:
        print('Число не найдено')


find_four(m)  # вывод

find_four(m)  # вывод
