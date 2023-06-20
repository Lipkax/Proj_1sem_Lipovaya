# Создайте базовый класс "Человек" со свойствами "имя", "возраст" и "пол". От этого
# класса унаследуйте классы "Мужчина" и "Женщина" и добавьте в них свойства,
# связанные с социальным положением (например, "семейное положение",
# "количество детей" и т.д.).


class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Man(Human):
    def __init__(self, name, age, family_status, number_of_children):
        super().__init__(name, age, "male")
        self.family_status = family_status
        self.number_of_children = number_of_children


class Woman(Human):
    def __init__(self, name, age, family_status, number_of_children):
        super().__init__(name, age, "female")
        self.family_status = family_status
        self.number_of_children = number_of_children


man1 = Man("Андрей", 28, "женат", 3)
woman1 = Woman("Катя", 22, "замужем", 1)

print(man1.name)  # Андрей
print(woman1.family_status)  # замужем
