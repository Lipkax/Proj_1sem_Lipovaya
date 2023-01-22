# 1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Индекс первого максимального элемента:
# Произведение элементов средней трети:
l = ['-44 2 12 22 1 43 120 -10 17']  # Запишем в файл data_1.txt список
f1 = open('data_1.txt', 'w')
f1.writelines(l)
f1.close()

f2 = open('data_2.txt', 'w')  # Дублируем список в новый файл data_2txt
f2.write('Исходные данные: ')
f2.writelines(l)
f2.close()

f3 = open('data_1.txt')  # преобразуем строку в числа
k = f3.read()
k = k.split()
for i in range(len(k)):
    k[i] = int(k[i])
f3.close()

f2 = open(
    'data_1.txt')  # Ищем максимальный элемент и количество элементов в файле data_1.txt и записываем в файл data_2.txt
max, t = 0, 0
for i in range(len(k)):
    max = max if max > k[i] else k[i]
if k[i] < 0:
    t += 1

f2 = open('data_2.txt', 'a')  # открываем файл для дозаписи
f2.write('\n')
print('Количество элементов: ', len(k), '\nИндекс первого максимального числа: ', max, file=f2)
f2.close()


def multiply(lst):
    answer = 1
    for i in lst:
        answer *= i
    return answer


f1 = open('data_1.txt', 'r', encoding='UTF-8').read()
umn = multiply([int(i) for i in f1.split(' ')[3:6]])  # умножение средней трети

print('Умножение средней трети: ', umn)

f2 = open('data_2.txt', 'a')
f2.write(f'Умножение средней трети: {umn}')
f2.close()  # закрываем файл
