# 2.Составить список, в который будут включены только согласные буквы и привести
# их к верхнему регистру. Список: ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели',
# 'Каир']
s = ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 'Каир']
fin = [c.upper() for c in ''.join(s).lower() if c in 'бвгджзйклмнпрстфхцчшщ']
print(fin)
