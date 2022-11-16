from random import randint  #импортирование модуля рандомных чисел   #обработка исключений
try:  #обработка исключений
        N = randint(10,20)
        A = [randint(1,10) for i in range(N)]
        print('Наш список:')
        print(A)

        print('Нечётные по порядку: ')
        print(A[::2])

        print("Чётные в обратном порядке: ")
        print(A[-1::-2])
        break
    except ValueError:
        print('Ошибка!')