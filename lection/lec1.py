'''
кооментарии
можно 
делать
тремя ковычками
с двух сторон

'''

# 
# ТИПЫ ДАННЫХ:
# int, float(вещественные), boolean, str, list, None

# как посмотреть тип переменной:
# через type: print(typy(переменная))

# a = None # отсутствие данных
# print(type(a))
# a = 1 # int, целое число
# print(type(a))
# a = 1.0 # float, число с плавающей запятой
# print(type(a))
# a = 1 + 1j # complex комплексное число
# print(type(a))
# a = '1' #str строка
# print(type(a))
# a = [1, 1, 'a'] # list список
# print(type(a)) 
# a = (1, 1 , 'a') # tuple кортеж
# print(type(a))
# a = {1, 1 , 'a'} # set множества
# print(type(a))
# a ={'a':1, 'b':2} # dict словарь
# print(type(a))
# a = True  # bool логическое булевое значение
# print(type(a))
'''
Конвертация переменных:

x = input('Ввод ') 
r = x + 5 
#print(type(x)) # <class 'str'>
print(r) #can only concatenate str (not "int") to str - т.к. строка


чтобы перевести строку в целое число используем int:

x = input('Ввод ') 
r = int(x) + 5 
#print(type(x)) # <class 'str'>
print(r) 


чтобы перевести строку в число с плавающей запятой используем float:

x = input('Ввод ') 
r = float(x) + 5 
#print(type(x)) # <class 'str'>
print(r)



int и float  могут конвертировать числа:
int(5.9) - будет 5
float(5) - будет 5.0

x = float(input('Введите число ')) 
y = float(input('Введите число ')) 
r = x + y
print('Результат '  + str(r)) 
'''


# ПЕРЕМЕННЫЕ - В пайтоне применяется два типа наименования переменных: camel case (userName)и underscore notation(user_name).
'''
переменные могут начинаться с букв, _, содержать алфавитно-цифровые символ _, не не должны совпадвть с ключевыми словами:
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
'''
#объявление переменных
#value = None # объявление переменной без без определения типа
# a = 123
# b = 1.23
# print(a)
# print(b)
# value = 123456
# print(value)

# если 2 раза указать одну и туже переменнню, то присвоится второе значение
# number = 3
# number = 4
# print(number) # присвоится 4

# при такой записи разным переменным присваивается одно значение:
# num1 = num2 = 5
# print(num1, num2)

# множественное присвоение:
# num_1, num_2 = 5, 7
# print(num_1, num_2)

#можем менять значение в переменных(обмен):

# swap1 = 8
# swap2 = 9
# # swap1, swap2 = swap2, swap1 # 9 8
# swap1, swap2 = swap2, swap1 + swap2 # т.е. при обмене можно сразу и проводить вычисления - # 9 17
# print(swap1, swap2)
# # swap2 = swap2 - number запись аналогична swap2 -= number
# swap2 -= number # number из предыдущего примера
# print(swap2)

'''
#распаковка списка по переменным:

# если количество переменных и количество элементов списка равны, то каждой переменной присваивается значание
z, x, c = [1, 2, 3]
print(z) #1
print(x) #2
print(c) #3

#  если переменных меньше,чем элементов списка, то используем * (arg), в ту переменную, которую обозначим * войдут все "лишние" значения
z, x, *c = [1, 2, 3, 4, 5, 6]
print(z) #1
print(x) #2
print(c) # [3, 4, 5, 6]

z, *x, c = [1, 2, 3, 4, 5, 6]
print(z) #1
print(x) #[2, 3, 4, 5]
print(c)#6
'''





#объявить строку

# s = 'hello word'
# print(s)

'''
если строка имеет много символов, ее можем разбить на части и разместить их на разных строках кода. 
В этом случае вся строка заключается в круглые скобки, а ее отдельные части - в кавычки:


text = ("Laudate omnes gentes laudate "
        "Magnificat in secula ")
print(text)

'''


# Если же мы хотим определить многострочный текст, то такой текст заключается в тройные двойные или одинарные кавычки:

'''
Это комментарий
'''
text = '''Laudate omnes gentes laudate
Magnificat in secula
Et anima mea laudate
Magnificat in secula 
'''
#print(text)

'''
При использовани тройных одинарных кавычек не стоит путать их с комментариями: 
если текст в тройных одинарных кавычках присваивается переменной, то это строка, а не комментарий.
'''



# Управляющие последовательности в строке:
# Строка может содержать ряд специальных символов - управляющих последовательностей. Некоторые из них:

# \: позволяет добавить внутрь строки слеш

# \': позволяет добавить внутрь строки одинарную кавычку

# \": позволяет добавить внутрь строки двойную кавычку

# \n: осуществляет переход на новую строку

# \t: добавляет табуляцию (4 отступа)





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


# если необходимо ограничить количество цифр после запятой, используем функцию ROUND
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



#f = [1, 2, 3, 4]
# print(f)
# print(2 in f) # 2 содержится в f
# print(not 2 in f) #  проверка 2 не содержится в f

# факт четности числа

# is_odd = f[0] % 2 == 0 # 0 - ложь, 1 - истина
# is_odd = not f[0] % 2 # более правильный вариант записи
# print(is_odd)

"""
управляющие конструкции:

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
"""

############################################ циклы:

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


#########################################################################################################333

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

"""

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


срезы: 

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

"""


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

# arg = 2
# print(f(arg))
# print(type(f(arg)))