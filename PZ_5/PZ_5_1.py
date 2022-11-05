try:  # обработчик исключений
    end = 60  # последнее число
    seq = range(end + 1)  # последовательность цифр
    s = sum(seq)  # функция суммы

    print("Сумма:", s)  # вывод суммы
except ValueError:
    print("Ошибка")
