# ФАЙЛЫ 
# как работать с файлами:
# связать файловую переменную с файлом, определив модификатор работы
#  a открытие для добавления данных
#  r открытие для чтения данных
#  w открытие для записи данных
#  w+ r+ 


# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') # текстовая переменная data, связываем с текстовым файлом
# #data.writelines(colors) # разделителей не будет
# data.write('Line 2')
# data.write('Line 3')
# data.close()

#еще один вариант записи данных:
# with open('file.txt', 'a') as data:
#     data.write('LINE 12\n')
#     data.write('LINE 122\n')


# exit() # код написанный после этой команды не выполняется
#чтение данных из файла:
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()


# ФУНУЦИИ
# это фрагмент программы используемый многократно
#  def function_name(x):
     # body line 1
     # ....
     # body line n
     # opyional return

'''
 ПРИМЕРЫ КОНЕЧНЫХ ФУНКЦИЙ:

 def sum(x):
    return x + 10 

def sum1(x):
    return x + 22
 
def sum3(x):
    return x + 242
 
def mult(x):
     return x**2

def mult2(x):
     return x**3

def mult3(x):
     return x**5

'''



# можно использовать функции из других файлов: 

# import lec 
# print(lec.f(1)) 

# import lec as l # можно писать не полностью название файлф, а записать сокращенно: as l(те. первая буква)
# print(l.f(1))


# ЗНАЧЕНИЯ ПО УМОЛЧАНИЮ ДДЯ ФУНКЦИЙ

#def new_string(symbol, count):
# def new_string(symbol, count = 3): # ставим второй аргумент по умолчанию
#     return symbol * count

# print(new_string('!', 5))   # !!!!!
# print(new_string('!'))      # TypeError missing 1 required... - ошибка, т.к. нет второго аргумента. если ставим аргумент по умолчанию, ошибки не будет
# print(new_string('!')) 
# print(new_string(4)) 


# ВОЗМОЖНОСТЬ ПЕРЕДАЧИ  ЛЮБОГО "НЕОГРАНИЧЕННОГО" КОЛИЧЕСТВА АРГУМЕНТОВ, для этого перед функцией ставим *

# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res

# print(concatenatio('a', 's', 'd', 'w'))  #asdw
# print(concatenatio('a', '1'))  # a1
#print(concatenatio(1, 2, 3, 4)) # TypeError, т.к. здесь используем строки

# если нужно использовать цифры:
# def concatenatio(*params):
#     res = 0
#     for item in params:
#         res += item
#     return res
# print(concatenatio(1, 2, 3, 4))



#РЕКУРСИЯ
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# list = []
# for e in range(1, 11):
#     list.append(fib(e))
# print(list) # 1 1 2 3 5 8 13 21 34



#КОРТЕЖИ:
# Кортежи - неизменяемый "список"

# t =()
# print(type(t))                #tuple - тип кортеж

# t = (1,)
# print(type(t))                #tuple - тип кортеж             

# t = (1)
# print(type(t))                # int

# t = (28, 9 , 1990)           #tuple - тип кортеж   
# print(type(t))

# colors = ['red', 'green', 'blue']
# print(colors)               #['red', 'green', 'blue']

# t = tuple(colors)
# print(t)                   # ['red', 'green', 'blue']


# пример записи кортежа:

# a = (3, 4, 41, 5) 
# print(a)
# print(a[-2])


# t = tuple(['red', 'green', 'blue'])
# print(t[0])    #red
# print(t[2])    # blue
# # print(t[10])  # ошибка - IndexError: tuple index out of range
# print(t[-2])    #green
# print(t[-200])  # ошибка IndexError: tuple index out of range
# t[0] = 'black' #  TypeError: 'tuple' object does not support item assignment    ошибка, в кортеж нельзя добавить элементы

#цикл для кортежа:
# for e in t:
#     print(e)    #red, green, blue



# распаковка кортежа, приобразование в переменные
# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))
#r:red g:green b:blue


#СЛОВАРИ неупорядоченные коллекции произвольных объектов с доступом по ключу

# dictionary = {}
# dictionary = \
#     {
#         'up': '↑'
#         'left': '←'
#         'down': '↓'
#         'right': '→'
#     }
# print(dictionary) # 'up': '↑' 'left': '←' 'down': '↓' 'right': '→'
# print(dictionary['left']) # '←' 
# #типы ключей могут отличаться

# #посмотреть все ключи
# for k in dictionary.keys():
#     print(k)                    #'up' 'left' 'down''right'

# #посмотреть значения:
# for k in dictionary.values():
#     print(k)                     #'↑'  '←'  '↓'  '→'

# # пробежаться по всем элементам словаря:
# for k in dictionary:
#     print(dictionary[values])

# #изменение элемента:
# dictionary['up'] = 'up'
# print(dictionary['up'])


#МНОЖЕСТВА

# add - добавить
# remove  - удалить элемент множества
# discard - удаление элемента, но если такого нет - ошибку не вызовет


# colors = {'red', 'green', 'blue'}
# print(colors)                     #{'red', 'green', 'blue'}

# colors.add('red')
# print(colors)                     #{'red', 'green', 'blue'}

# colors.add('gray')
# print(colors)                     #{'red', 'green', 'blue', 'gray}

# colors.remove('red')
# print(colors)                     #{'blue', 'green', 'gray'}

# colors.remove('red')
# print(colors)                    #KeyError: 'red'

# colors.discard('red')          #ok
# print(colors)


# Операции с множествами
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()           #c = {1, 2, 3, 5, 8} копируем
# u = a.union(b)         # u =  {1, 2, 3, 5, 8, 13, 21} объединение
# i = a.intersection(b)   # i = {8, 2, 5} 
# dl = a.difference(b)    # dl = {1, 3}
# dr = b.difference(a)    # dr = {13, 21}

# q = a\
#     .union(b)\
#     .difference(a.intersection(b))
# #{1, 21. 3, 13}

# # замороженное множество
# s = frozenset(a)



#СПИСКИ - если 2 списка равны, то при смене элемент ов в одном списке, элементы меняются и в другом(без разницы в каком менять)

# list1 = [1, 2, 3, 4, 5]
# list2 = list1
# list1[0] = 123
# list2[1] = 333

# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)

# list1[0] = 123

#как можно удалять последний элемент списка:

# list1 = [1, 2, 3, 4, 5]

# print(len(list1))
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)

# удалить конкретный элемент из списка:

# list1 = [1, 2, 3, 4, 5]
# print(len(list1))
# print(list1.pop(2)) # указываем под каким индексом удалить элемент
# print(list1)

#вставить на нужную позицию элемент:
# list1 = [1, 2, 3, 4, 5]
# print(list1.insert(2, 11))
# print(list1)


#добавление в конец списка: append
list1 = [1, 2, 3, 4, 5]
print(list1.append(11))
print(list1)