# оператор except - позволяет обработать ошибки
# оператор finally - работает всегда, позволяет сохранить данные, даже если прогрмма "завалилась"(например: непредвиденная ошибка)

# while True:
#     try:
#         enter = float(input('Введите число: '))
#         print(100/enter)
#     except ValueError:
#         print('Вы ввели не число!!!')
    
#     except ZeroDivisionError:
#         print('Ltkbnm на ноль нельзя!!!')
    
#     else:
#         print('Пользователь молодец, с первого раза!!!')

#     finally:
#         print('Вывод финали')

# print('Все норм')

"""
пример
"""

import sys
url_list = ['text_1.txt', 'text_2.txt', 'txt_25.txt', 'text_3.txt']

list_defect = []
list_info = []
try:
    for url in url_list:
        try:
            r=open(url, encoding='utf-8')
            list_info.append(r.read())
            print('Where') 

        except Exception: #(все ошибки типа FileNotFoundError, TypeError, ValueError)
            list_defect.append(url)
            print('Here')
            #sys.exit() # экстренное закрытие программы. метод генерирует особую ошибку
            continue
finally: # сохраняем наши данные
    r = open('save.txt', 'a', encoding='utf-8')
    for i in list_info:
        r.write(i)
    r.write(str(list_defect))
    r.close()
    print('Я все записал, не смотря ни на что!!!!')

# print(list_defect) # ['txt_25.txt']
# print(list_info) # ['инфа из первого', 'инфа из второго', 'инфа из третьего']
    
