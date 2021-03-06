# словари
# создание


# d1 = {'a':7}
# print(d1) # просмотреть словарь
# print(d1['a']) # просмотреть значение по ключу

# ####################################### добавление значения в словарь

# d1['b'] = 9 
# print(d1) # {'a': 7, 'b': 9}


# ################################## # поменять значение по ключу
# d1['a'] = 8 
# print(d1) # {'a': 8, 'b': 9}


# ####################################### удалить значение из словаря

# del d1['a']
# print(d1) #{'b': 9}



# ######## встроенная функция dict

# d2 = dict(a=7)
# print(d2) # {'a': 7}

# функция dict - конвертирующая функция - может создать словарь, из вложенных списков со вложенными списками

# d3 = dict([[1,2],[3,4],[5,6]])
# print(d3) #{1: 2, 3: 4, 5: 6}



# ######## функция dict.fromkeys из ключей со значениями по умолчанию

# d3 = dict.fromkeys([1,2,3,4,5])
# print(d3) # {1: None, 2: None, 3: None, 4: None, 5: None}

# # можно указать второе значение по умолчанию:
# d3 = dict.fromkeys([1,2,3,4,5], 'value')
# print(d3) #{1: 'value', 2: 'value', 3: 'value', 4: 'value', 5: 'value'}

"""
price = { 'meat':3, 'bread':1, 'potato':0.5, 'water':0.2} # не считает?????

def buy():
    pay = 0
    while True:
        enter = input('что покупаем?\n')
        if enter == 'end':
            break
        pay  += price[enter]
    return pay

buy()

##########  пример: словарь в словаре. есть база данных пользователей, в которой есть пользователи, и эти пользователи отдельный словарь

users = {
    'Alex7':{'password': 9856214, 'id': 1957},
    'Jimmy99':{'password': 1236487, 'id': 9654},
    'Bob33':{'password': 9546752, 'id': 6453}
}

print(users['Alex7'] ['password'])
"""


# методы в словарях:
#словари изменяемый тип данных

# .copy - копируем словарь, если записать d1=d5, то изменяя один словарь, изменим и другой
# .items() - отображает словарь в виде кортежей - нужен для работы со словарем при помощи цикла for
# .keys() - возвращает ключи словаря в виде списка
# .values() - возвращает значения словаря в виде списка

# .update(указываем второй словарь) добавить пары ключ/значение из одного словаря в другой. если ключи совпадают - значения переписываются, т.е. заменяются


d1 = {'a':1, 'b':2}
d3 = dict([[1,2],[3,4],[5,6]])

# d5 = d1.copy
# print(d5)
# print(d1.items()) #([('a', 1), ('b', 2)])
# print(d1.keys()) #dict_keys(['a', 'b'])
# print(d1.values()) # dict_values([1, 2])
# d1.update(d3)
# print(d1) # {'a': 1, 'b': 2, 1: 2, 3: 4, 5: 6}


###################### если ключа в словаре нет - вернется ошибка:

#print(d1['c']) # KeyError: 'c'

# .get  чтобы ошибки избежать 

# y = d1.get('c')
# print(y) # None - если такого значения нет

##################или можно его туда добавить, если его там нет:

# y = d1.get('c', 'value')
# print(y) # value

###############   .pop() позволяет удалить из словаря пару ключ/значение и вернуть это значение в переменную
t = d1.pop('a') 
print(t, d1) # t = 1, d1 = {'b': 2}