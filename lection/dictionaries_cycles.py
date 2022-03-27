# исполбзование циклов

# если поместить в цикл for словарь - итерироваться будут его ключи


# price = { 'meat':3, 'bread':1, 'potato':0.5, 'water':0.2}

# # for i in price:
# #     print(i) 

#####################################################

# # если необходимо использовать значения, можно обращаться к индексам:
# # например, установим скидку 15% на товар

# for i in price:
#     price[i] = round(price[i] * 0.85, 2) # округляем до 2 цифр после запятой

# print(price) # {'meat': 2.55, 'bread': 0.85, 'potato': 0.42, 'water': 0.17}

"""
создадим на основе нашего словаря новый словарь

price = { 'meat':3, 'bread':1, 'potato':0.5, 'water':0.2}

new_price = {}

for i in price:
    new_price[i] = round(price[i] * 0.85, 2)
print(price) # {'meat': 3, 'bread': 1, 'potato': 0.5, 'water': 0.2}
print(new_price) # {'meat': 2.55, 'bread': 0.85, 'potato': 0.42, 'water': 0.17}
"""

# метод .items - - отображает словарь в виде кортежей - нужен для работы со словарем при помощи цикла for

#price = { 'meat':3, 'bread':1, 'potato':0.5, 'water':0.2}


# x = price.items()
# print(x) # dict_items([('meat', 3), ('bread', 1), ('potato', 0.5), ('water', 0.2)])

# print(type(x)) #<class 'dict_items'>

#  ##### можно преобразовать в список
# print(list(x)) # [('meat', 3), ('bread', 1), ('potato', 0.5), ('water', 0.2)]

#################################### пример 


# ######  получаем кортеж
# for i in price.items():
#     print(i)       # ('meat', 3)
#                    #('bread', 1)
#                    #('potato', 0.5)
#                    #('water', 0.2)


# ####### чтобы распаковать кортеж:

# for key, value in price.items():
#     print(key)
#     print(value)   # meat
#                    # 3
#                    # bread
#                    #  1
#                    # potato
#                    #  0.5
#                    # water
#                    # 0.2


###################  поменять местами значения и ключ

# new = {}
# for key, value in price.items():
#     new[value] = key
# print(new) # {3: 'meat', 1: 'bread', 0.5: 'potato', 0.2: 'water'}

"""
.values()  - возвращает в виде списка значения словаря

price = { 'meat':3, 'bread':1, 'potato':0.5, 'water':0.2}


x = price.values()
print(x)   # dict_values([3, 1, 0.5, 0.2])
print(type(x)) # <class 'dict_values'> объект отображения словаря

# преобразовать в лист:
print(list(x)) # [3, 1, 0.5, 0.2]


применение цикла for:


#№№№№№№ итерируем по значениям: 
# например для поиска средней цены и тп

for value in price.values():
    print(value)    #3
                    #1
                    #0.5
                    #0.2

"""


# .keys - для работы с ключами - в данном случае для экономии вычмслительных мощностей. 




price = { 'meat':3, 'bread':1, 'potato':0.5, 'water':0.2}

# x = price.keys()
# print(x) # dict_keys(['meat', 'bread', 'potato', 'water'])


new_price = {}

for i in price.keys():
    new_price[i] = round(price[i] * 0.85, 2)
#print(price)
print(new_price) # {'meat': 2.55, 'bread': 0.85, 'potato': 0.42, 'water': 0.17}
