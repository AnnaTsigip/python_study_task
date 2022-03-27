# h = [9,8,7,4,5,6,3,2,1,5,5]


# #создадим новый список:

# newh = []
# for x in h:
#     newh.append(x*2)
# print(newh) # [18, 16, 14, 8, 10, 12, 6, 4, 2, 10, 10]

# #####################################################################

# #создадим новый сисок при помощи генератора:
# newh2 = [x*2 for x in h]

# # множества:
# z= { x*2 for x in h}

# # словарь
# f= {x: x*2 for x in h}


# print(newh)  # [18, 16, 14, 8, 10, 12, 6, 4, 2, 10, 10]
# print(z) # {2, 4, 6, 8, 10, 12, 14, 16, 18}
# print(f) # {9: 18, 8: 16, 7: 14, 4: 8, 5: 10, 6: 12, 3: 6, 2: 4, 1: 2}


'''
в генераторе можно добавлять условия

h = [9,8,7,4,5,6,3,2,1,5,5]


newh = []
for x in h:
    if x%2 == 0:
        newh.append(x*2)
print(newh) # [16, 8, 12, 4]


g = [x for x in h if x%2 == 0]
print(g) # [8, 4, 6, 2]
'''

# генератор может содержать вложенные циклы
# если запись длинная можно переносить на другую строку
#парсер файлов в генераторе


# import os

# g = [os.path.join(z,i)
#     for z, x, c in os.walk('C:\\')
#     for i in c if '.txt' in i]
# print(len(g))
# print(g)


"""
генератор словаря на основании другого словаря
"""

price = { 'meat':2, 'bread':1, 'potato':0.5, 'water':0.2}

new_price = {}
for i in price.keys():
    new_price[i] = round(price[i] * 0.85, 2)

print(new_price) # {'meat': 1.7, 'bread': 0.85, 'potato': 0.42, 'water': 0.17}


# через генератор словаря

new_d = {i: round(price[i] * 0.85, 2) for i in price.keys()}
print(new_d) # {'meat': 1.7, 'bread': 0.85, 'potato': 0.42, 'water': 0.17}