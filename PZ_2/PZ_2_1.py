#дано двузначное число. Вывести число, полученное при перестановке цифр исходного кода.

try: #обработчик исключений
    a = int(input("Введите двухзначное число ")) #ввод числа
    b = a//10 #нахождение первой цифры
    print(f'Вывод B: {b}')  #вывод переменной
    c = (a % 10)*10 #нахождение второй цифры
    print(f'Вывод C: {c}') #вывод переменной
    print(f'Полученное число: {c + b}') #вывод сложения двух переменных
except: #обработка исключений
    print("Ошибка!!") #вывод ошибки