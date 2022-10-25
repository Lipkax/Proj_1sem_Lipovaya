# if ((i mod 4 = 0)and (i mod 100<>0))or(i mod 400 = 0)
n = int(input("Введите номер год "))
A = "не високосный"
if (n % 4 == 0) and not (n % 100 == 0 and n % 400 != 0):
    A = "високосный"
    print(n, " : ", A)

    if (n % 4 == 0) and (n % 100 != 0 or n % 400 == 0):
        A = "високосный"
    print(n, " : ", A)






