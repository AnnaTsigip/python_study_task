# нонимные lamnda функции

# def f(x):
#     return x**2

# g = f # в переменную можем положить в функцию

# print(type(f))
# print(type(g)) # у функции  и переменной, в которую положили ссылку на функцию - один тип   <class 'function'>

# print(f(4))
# print(g(4)) # соответственно и результат одинаков - 16

'''
math

# берем 2 функции:
def calc(x):
    return x+10
#print(calc(10))


def calc2(x):
    return x*10
#print(calc2(10))


def math(op, x): # в функцию math можно положить другию функцию в виде операции 
    print(op(x))

math(calc2, 10)
math(calc, 10)

'''


#lambda

from ast import Lambda
from tkinter import W


# def sum(x,y):
#     return x+y

#f = sum # можем в переменную положить функцию
#sum = lambda x, y: x + y # запись аналогична : def sum(x,y): return x+y   и f = sum
#     



# def mylt(x,y):
#     return x*y

# def calc(op, a, b):
#     print(op(a,b))
#    # return (op(a, b))

# calc(mylt, 4, 5) #передаем в функцию calc в качестве аргумента функцию mylt 

# #calc(f, 4, 5) # f = sum
# #calc(sum, 4, 5) #sum = lambda x, y: x + y
# calc(lambda x, y: x + y, 4, 5)

'''
List Comprehension 
[exp for item in iterable]
[exp for item in iterable (if conditional)]
[exp <if conditional> for item in iterable(if conditional)]

#список четных чисел от 1 до 20

# list = []

# for i in range(1, 21):
#     if(i%2 == 0):
#         list.append(i)

# print(list)

#или можно так:

# list = [i for i in range (1,21) if i % 2 == 0] 
# print(list)

# # с использованием картежа:

# list = [(i,i) for i in range (1,21) if i % 2 == 0]  # (i,i) - обозначение кортежа
# print(list)

# #с функцией:

def f(x):
    return x**3

list = [f(i) for i in range (1,21) if i % 2 == 0]  # будут перебираться все числа от 0 до 20, далее проверяться на четность, четные возводиться в куб
print(list)


#кортеж

list = [(i, f(i)) for i in range (1,21) if i % 2 == 0]  # будут перебираться все числа от 0 до 20,
# далее проверяться на четность, четные возводиться в куб, выводятся на экрат кортеж - число и его куб
print(list)
'''

# # Ананимные, lambda функции
# # задача:
# # в файле хранятся числа, нужно выбрать четные и составить список пар(число; квадрат числа).

# #path = 'file.txt'
# f = open('file.txt','r')
# data = f.read() + ' '
# f.close

# numbers = []

# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos+1:]

# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e, e **2))
# print(out)




# БЕЗ ФАЙЛА

# def select(f,col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()

# res = select(int, data)
# res = where(lambda x: not x % 2, res)
# res = select(lambda x: (x, x**2), res)
# print(res)

''' ФУНКЦИЯ map:
функция map() применяет указанную функцию к каждому элеменнту интерируемого объекта и возвращает итератор с новыми объектами.

f(x)  x+10
map(f,[1,  2,  3,  4,  5])
       11, 12, 13, 14, 15
Нельзя пройтись дважды

# li = [x for x in range(1,20)]
# li = list(map(lambda x:x+10, li)) # изменяем первоначальный список на +10
# print(li)

#ЕЩЕ ПРИМЕР ИСПОЛЬЗОВАНИЯ map

#data = list(map(int, input().split())) # преобразование чисел в лист
    #print(data)

#data = map(int, input().split()) #можем в лист не преобразовывать, а сразу пробежаться по соответствующим объектам

# data = map(int, '1 2 3 4 55 68'.split()) # можем сразу ввести данные в строку, далее преобразовать их в числа
# for e in data:
#     print(e)

# data = list(map(int, '1 2 3 4 55 68'.split())) # если нужно использовать данные map несколько раз, сразу необходимо писать list

'''


#Функция filter:
# функция filter() применяет указанную функцияю к каждому элементу итерируемого объекта и возвращает итератор с теми объектами,
# для которых функция вернулв true

# f(x)  x - четное
# filter(f, [ 1, 2 , 3,  4, 5 ])
#           [  2,  4]
# НЕЛЬЗЯ ПРОЙТИСЬ ДВАЖДЫ

# data = [x for x in range(10)]
# res = list(filter(lambda x: not x % 2, data))
# print(res)

'''
исправим код с использованием map, filter

data = '1 2 3 5 8 15 23 38'.split()

res = map(int, data) # заменили select 
res = filter(lambda x: not x % 2, res)
res = list(map(lambda x: (x, x**2), res)) # заменили select 
print(res)
'''

# Функция zip
#  Функция zip() применяется к набору итерируемых объектов и возвращает итератор с кортежами из элементов входных данных.

#  количество элементов в результате равно минимальному количеству элементов входного набора
#  zip ([1, 2,3], ['о', 'д', 'т'], ['f', 's', 't'])
#     [(1,'о', 'f'), (2, 'д', 's'), (3, 'т', 't')]

# НЕЛЬЗЯ ПРОЙТИСЬ ДВАЖДЫ

# users = ['user1', 'user2', 'user3','user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]

# data = list(zip(users, ids)) 
# #data = list(zip(users, ids, salary)) # усли один из наборов меньше остальных, то итоговый список равен ешго длине, т.е. длине минимального
# print(data)


'''
функция enumerate 
функция enumerate() применяется к итерируемому объекту и возвращает новый итератор с кортежами из индекса и элементов входных данных

enumerate (['Казань', 'Смоленск', 'Рыбки', 'Чикаго'])
[(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбки'), (3, 'Чикаго')]

НЕЛЬЗЯ ПРОЙТИСЬ ДВАЖДЫ

Пример:

users = ['user1', 'user2', 'user3','user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]

data = list(enumerate(users)) 
print(data)


'''
