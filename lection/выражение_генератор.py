h = ['https:\\www.сайт.com', 'https:\\www.какойтосайт.com', 'https:\\www.левыйсайт.com',
    'https:\\www.ещесайт.com', 'https:\\www.другойсайт.net', 'https:\\www.исновасайт.com']


# # генератор списка - сразу выгружает новый список в память. 

# # #генерируем список сайтов по условиям
# n = [x.split('\\')[1] for x in h if '.com' in x] 
# # print(n) # ['www.сайт.com', 'www.какойтосайт.com', 'www.левыйсайт.com', 'www.ещесайт.com', 'www.исновасайт.com']
# # print(type(n)) # <class 'list'>

# #к генератору списка можем обращаться к элементу по индексу, можем вызывать срез
# print(n[1]) #www.какойтосайт.com

'''
# выражение генератор 

z=(x.split('\\')[1] for x in h if '.com' in x)
#print(type(z)) # <class 'generator'>

# выражение генератор возвращает по одному значению при каждом обращении. т.е. в памяти нет списка z[1] - ошибка 
 
# for i in z:
#     #print(i)      #www.сайт.com
#     #             www.какойтосайт.com
#     #             www.левыйсайт.com
#     #             www.ещесайт.com
#     #             www.исновасайт.com


# чтобы появилось значение, его нужно запросить:

print(next(z)) # www.сайт.com
print(next(z)) # www.какойтосайт.com
print(next(z)) # www.левыйсайт.com
'''

import os
# n = [x for x in os.walk('C:\\')] # генератор списка
# print('здесь') # выгрузится весь список

z= (y for y in os.walk('C:\\')) # выражение генератор
print('тут') 

#print(len(n)) # можем посмотреть длину списка # генератор списка 

##print(n.__sizeof__()) # сколько места занимает в памяти  генератор списка
print(z.__sizeof__()) # сколько места занимает в памяти выражение генератор

# выдача по одному элементу за раз:

print(next(z)) #('C:\\', ['$Recycle.Bin', '360SANDBOX', 'Documents and Settings', 'Intel', 'PerfLogs', 'Program Files', 'Program Files (x86)', 'ProgramData', 'Recovery', 'System Volume Information', 'Users', 'Windows'], ['hiberfil.sys', 'pagefile.sys', 'swapfile.sys'])
                #PS C:\Users\User\python>

print(next(z)) # ('C:\\$Recycle.Bin', ['S-1-5-18', 'S-1-5-21-1009357132-2771681914-1473080898-1001'], [])
                #PS C:\Users\User\python>