# Даны три целых числа: A,В,C. Проверить истинность высказывания "Хотя бы одно из чисел A,В,C положительное"
try:  # обработчик исключений
    a, b, c = int(input("Введите A: ")), int(input("Введите число В: ")), int(input("Введите число С: "))  # ввод чисел
    print((a > 0)) and (b > 0) and (c > 0)  #выводим, если одно из чисел положительное
except:  # обработчик исключений
    print("False")  #выводим, если условие не выполняется
