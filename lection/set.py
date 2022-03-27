# множества могут состоять из неизменяемых типов данных: число, кортеж, строка:
#множества неупорядоченная коллекция  уникальных элементов:

# t = {'a', 'f', 1, 2, 3, (2, 5)}

# print(t)

"""
если взять:


# посмотрим сколько памяти занимает какой тип данных при помощи метода  __sizeof__()
x= (1, 2, 3, 4, 5, 6, 7) # кортеж
y= [1, 2, 3, 4, 5, 6, 7] # список
u={'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7} # словарь
h={1, 2, 3, 4, 5, 6, 7} # множества

print(x.__sizeof__())  # 80
print(y.__sizeof__()) #104
print(u.__sizeof__()) # 344
print(h.__sizeof__()) # 456

"""


# примеры мспользования:
# сравнение затраченного времени при работе со списками и с множествами:
# import time

# def f(*args):
#     list_new = []
#     for i in args:
#         for y in i:
#             if y not in list_new:
#                 list_new.append(y)
#     return list_new

# z = list(range(10000))
# x = list(range(5000, 15000))
# c = list(range(10000, 20000))



# start = time.time()
# f(z,x,c)
# stop = time.time() - start
# print(stop) # 6.814768552780151


# start2 = time.time()
# r=set(z)
# t=r.union(set(x), set(c))
# stop2 = time.time() - start2
# print(stop2) # 0.004998445510864258

"""
методы множеств:
  .add ()  позволяет добавить в множество какой-то элемент
  .discard() позволяет удалять элементы из множества. если такого элемента в множестве нет- ошибки не будет
  .remove() позволяет удалять элементы из множества. если такого элемента в множестве нет- будет ошибка
                           z.remove(7) #{1, 2, 3, 4}
                           KeyError: 7
объединение:
y = z.union(x) (y - в какое множество объединяем, (х) с каким множеством объединяем)
z.update(x) - объединение множеств. к z добавили х

пересечение множеств:
t=z.intersection(x)  в новую переменную сохраняем пересечение

разница множеств:

e = z.difference(x)  z-x 

*************************************************


z={1,2,3,4,5}
x={3,4,5,6,7}

z.add (6) # {1, 2, 3, 4, 5, 6}
z.discard(6) # {1, 2, 3, 4, 5}
#z.remove(5) # {1, 2, 3, 4}
#y = z.union(x) # {1, 2, 3, 4, 5, 6, 7}
#z.update(x) # {1, 2, 3, 4, 5, 6, 7}
t = z.intersection(x) # {3, 4, 5}
e = z.difference(x) # {1, 2}

print(e)

"""

# пример использования множеств:
# метод .split() который вернет список из всех слов (текста из файла) все пробеды и знаки переноса строки откинет
# преобразуем во множество: функциия set

# new = set()

# r = open('text_set.txt', encoding='utf-8')
# new.update(set(r.read().split()))
# r.close()

# r = open('text_set2.txt', encoding='utf-8')
# new.update(set(r.read().split()))
# r.close()

# print(new)
#n***********************************************************************************************8

# посмотреть одинаковые элементы: {'и', '—', 'Большинство', 'есть', 'на'}


# r = open('text_set.txt', encoding='utf-8')
# r1 = set(r.read().split())
# r.close()

# r = open('text_set2.txt', encoding='utf-8')
# r2 = set(r.read().split())
# r.close()

# new= r1.intersection(r2)
# print(new)

#*****************************************************************************8

# разницу:

r = open('text_set.txt', encoding='utf-8')
r1 = set(r.read().split())
r.close()

r = open('text_set2.txt', encoding='utf-8')
r2 = set(r.read().split())
r.close()

new= r2.difference(r1)
print(new)