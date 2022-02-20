# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

#find(str[, start [, end]): происходит возвращение индекса подстроки в строку в Python.
#В том случае, если подстрока не найдена, выполняется возвращение числа -1;


# line = 'qwe, asd, zxc, qwe, ertqwe'
# element = input('Введите element: ')
# index = line.find(element)
# print(index)

# 2 входа: 

line = 'qwe, asd, zxc, qwe, ertqwe'
element = input('Введите element: ')
if line.count(element) == 1:
    print(f'{element} в строке встречается 1 раз')
elif line.count(element) < 1:
    print(f'{element} в строке НЕ встречается')
else:
    print(line.find(element, line.find(element) + 1))

