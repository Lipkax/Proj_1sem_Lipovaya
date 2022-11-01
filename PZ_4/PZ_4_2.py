try:  # обработчик исключений
    N = input("Введите целое число N : ")  # ввод числа
    K = 0
    S = 0
    while int(N) >= int(S):  # цикл while
        K += 1
        S += K
    print("K = ", K, "S =", S)  # вывод чисел
except ValueError:  # обработчик исключений
    print("Ошибка")  # вывод ошибки
