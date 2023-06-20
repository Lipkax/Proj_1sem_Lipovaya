# Вариант 13.
# Создайте класс "Компьютер" с атрибутами "марка", "процессор" и "оперативная
# память". Напишите метод, который выводит информацию о компьютере в формате
# "Марка: марка, Процессор: процессор, Оперативная память: память".

class Komputer:
    def __init__(self, stamp, processor, ram):
        self.__stamp = stamp
        self.__processor = processor
        self.__ram = ram

    def get_info(self):
        return print(f"Марка: {self.__stamp}, Процессор: {self.__processor} , Оперативная память: {self.__ram}")


my_komp = Komputer("MSI", "Intel Core i7", "16 ГБ")
print(my_komp.get_info())

