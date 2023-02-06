# Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее
# элементов.
from random import randint

len_m = int(input('Введите размер матрицы: '))  # ввод размер матрицы

m = [[randint(-20, 20) for _ in range(len_m)] for _ in range(len_m)]  # создание матрицы
for row in m:
    print(*row)
    print()

for i in range(len(m)):  # вычисление среднего арифмитического с нечетным номером
    if i % 2 != 0:
        sum_m = sum(m[i]) / len(m[i])  # среднее арифметическое
print('Среднее арифметическое: ', sum_m)
