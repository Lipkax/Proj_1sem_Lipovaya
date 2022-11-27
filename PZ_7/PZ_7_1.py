# Дана строка. Подсчитать количество содержащихся в ней цифр.
try:  # проверка исключений
    s = 'aaaabbbacc7cAAAcd43884d'  # строка символов
    number = 0  # создаем начальное количество цифр
    for i in s:
        if i in '1234567890':
            number += 1  # если перебираемая строка содержит символ равный 1-10, то добавляем к намбер 1
    if i in '':
        number += 'В строке нет цифр'  # если не цифра то выводиться "В строке нет цифр"
        print(number)
except ValueError:
    print("Ошибка")
