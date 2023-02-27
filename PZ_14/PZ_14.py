# импорт библиотеки re
import re
f1 = open('dates1.txt', 'r', encoding='UTF-8').read()  # открытие файла
f = re.sub(r'[.]', r'/', f1)  # регулярное выражение
f2 = open('dates2.txt', 'w', encoding='UTF-8')  # открытие файла на запись
f2.writelines(f)  # запись в файл
f2.close()



