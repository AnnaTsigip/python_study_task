# x = 7
# print(dir()) # какие нам сейчас доступны функции



# from lection.newmod import newf
# import newmod

# #print(dir(newmod)) # ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'k', 'k2', 'newf'] 
#                     #смотрим доступные имена и функции в модуле newmod

# print(help(newf)) # через help смотрим описание функции

'''
import newmod as n # импортируется полностью подуль к элементам обращаемся через имя модуля
print(newmod.newf(3)) # 3**2=9 используем функцию тогда вместо newnod пишем n   n.newf
k=10 
print(newmod.k) #7
print(k) #10    т.е. переменные k и newmod.k - разные переменные
'''


################################################################################################################

# или можно импортировать только необходимые элементы модуля, обращаемся сразу к необходимому элементу

# from newmod import * # импортируем полностью модуль

# print(k) #7
# print(newf(7)) #49

#print(dir())

###################################################################################################################

#импортировать отдельные элеметы:

# from newmod import newf # будет доступна только функция, переменные будут недоступны

# print(newf(7)) #49


'''
работа со встроенными модулями

1. import sys
2. from sys inport *
3. from sys import ___ указать что необходимо импортировать

print(sys.path) # посмотреть где на компе хранятся файлы с расширением .py
'''

# проверка __name__ == '__main__'
#т.к. при импорте имя меняется, то сразу он выполняться не будет, но можем использовать функционал

import newmod
#print(newmod.__name__) # newmod
print(newmod.newf(7)) #49
