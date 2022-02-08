# типы данных и переменная
# int, float(вещественные), boolean, str, list, None


#объявление переменных
#value = None # объявление переменной без без определения типа
# a = 123
# b = 1.23
# print(a)
# print(b)
# value = 123456
# print(value)

# как посмотреть тип переменной
# value = None
# print(type(value))
# a = 123
# b = 1.23
# print(type(a))
# print(type(b))
# value = 123456
# print(type(value))


#объявить строку

# s = 'hello word'
# print(s)

#слэш последовательности
# /n переход на новую строку

# варианты вывода в консоль
# a = 123
# b = 1.23
# s = 'hello word'
# print(a,b,s)
# print(a, '-',b, '-', s)
# print('{} - {} - {}'.format(a,b,s)) # по умолчанию переменные ставятся попорядку
# print('{2} - {0} - {1}'.format(a,b,s)) # если необходимо пеменять порядок вывода переменных указываем в {}
# print(f'{a} - {b} - {s}')

#логические переменные
# f = False
# c = True
# print (f,c)

# list - список(массив) варианты вывода
# list = []
# col = [1, 2, 3] #числа
# col2 = ['1', '2', '3'] #список строк
# print(list)
# print(col)
# print(col2)

#ввод и вывод данных
# print('введите a');
# a = int(input()) #если работаем с цифрами сразу указываем тип данных.
# т.к. по умолчанию работаем со строками, т.к. динамическая типизация
# print('введите b');
# b = int(input())
# print(a, b)
# print('{} {}'.format(a, b))
# print(a, '+' ,  b, ' = ' , a+b) #если сразу хотим произвести действия
# print(f'{a} {b}')

#Арифметические операции
# +, -, *, /, %,  //,  **,
# унарный минус - инверсия числа

# a = 123
# b = 322
# c = a + b
# print(c)

#по умолчанию считается по вещесттвенным числам
# a = 12
# b = 8
# c = a / b
# print(c)

# деление в целых числах //
# a = 12
# b = 8
# c = a // b
# print(c)

#остаток от деления %
# a = 12
# b = 8
# c = a % b
# print(c)


# возведение в степень **
# a = 2
# b = 8
# c = a ** b
# print(c)

# если необходимо ограничить количество цифр после запятой, используем функцию round

# a = 1.3123
# b = 3
# c = round(a * b, 3)
# print(c)

#сокращенные операции присваивания

#a = 3
# a = a + 5 - можем сократить запись на +=, аналогично это работает и с другими арифметическими операциями
# a +=5

# print(a)

#логические операции
# >, >=, <, <=, ==, !=
# not, and, or, не путать с &, |, ^
# и еще: is, is not, in, not in

# a = 1 < 4 and 5 > 2
# print(a)

#можно сравнивать строки
# a = 'qwe'
# b = 'qwe'
# print(a == b)

#можно сравнивать списки

# a = [1, 2]
# b = [1, 2]
# print(a == b)

# можно использовать тройные неравенство и более

# a = 1 < 3 < 5 <10
# print(a)

# func = 1
# T = 4
# x = 2
# print(func<T>(x))

#логические операции
# f = 1 > 2 or 4 < 6
# print(f)

#  in

#f = [1, 2, 3, 4]
# print(f)
# print(2 in f) # 2 содержится в f
# print(not 2 in f) #  проверка 2 не содержится в f

# факт четности числа

# is_odd = f[0] % 2 == 0 # 0 - ложь, 1 - истина
# is_odd = not f[0] % 2 # более правильный вариант записи
# print(is_odd)

#if, if-else

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)



# if, if-else

# username = input('Ведите имя: ')
# if username == 'Маша':
#     print('Ура, это же Маша')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - ТОП')
# else:
#     print('Привет, ', username)


#while
# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)


# while - else
# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй')
#     print('хватит')
# print(inverted)


# for

# for i in 1,2,3,4,5:
#     print(i**2)

# list = [1,2,3,4,5]
# for i in list:
#     print(i**2)

#range: перечисление от 0 до 9
# r = range(10)
# for i in r:
#     print(i)

# range можно записать:
# for i in range(5): # можем указать диапазон range(1, 5) т.е. от 1 до 4, можно обозначить шаг 
#     print(i)

# for i in range(1, 5): # можем указать диапазон range(1, 5) т.е. от 1 до 4, 
#     print(i)

# for i in range(1, 20, 2): #  можно обозначить шаг 
#     print(i)

# можно разбивать строки:
# for i in 'qwe - rty':
#     print(i)


#СТРОКИ

#text = 'съешь еще этих мягких француцских булок'
# print(len(text)) #определение количества символов функция len
# print('еще' in text) #наличие подстроки в строке
# print(text.isdigit()) #являются ли все символы строки числами
# print(text.islower()) #являются ли все символы строки символами нижнего регистра
# print(text.replace('еще','ЕЩЕ'))  # заменить

# for с in text:
#     print(с)


# Справка по функции: 
# help(text.istitle)

# text = 'съешь еще этих мягких француцских булок'
# print(text[0]) # с
# print(text[1]) # ъ
# print(text[len(text) - 1]) # к
# print(text[-5]) # б 
# print(text[:]) # print(text), т.е. по умолчанию от 0 до -1 символа
# print(text[:2]) # съ
# print(text[len(text) - 2:]) # ок
# print(text[2:9]) # ешь еще
# print(text[6: -18]) # еще этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] #


# списки: введение
# Список - пронумерованная, изменяемая коллекция объектов



# numbers = [1, 2, 3, 4, 5]
# print(numbers) # [1, 2, 3, 4, 5]

# numbers = list(range(1, 6))
# print(numbers) # [1, 2, 3, 4, 5]

# numbers[0] = 10
# print(numbers) # [10, 2, 3, 4, 5]

# for i in numbers:
#     i *= 2
#     print(i) # [20, 4, 6, 8, 10]
# print(numbers) #[10, 2, 3, 4, 5]


#добавить/удались элемент в списке:

# colors = ['red', 'green', 'blue']
# for e in colors:
#     print(e) # red green blue

# for e in colors:
#     print(e*2) # redred greengreen blueblue

# colors.append('gray') #добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') # или: del colors[0] # удалить элемент


# ФУНКЦИИ - фрагмент программы, используемый многократно
# def function_name(x):
    #body line 1
    # ....
    # body line n
    # optional return


def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 2
print(f(arg))
print(type(f(arg)))