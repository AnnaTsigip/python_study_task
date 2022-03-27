'''

#  'r' открыть для чтения (по умолчанию0)
#  't' открыть в текстовом режиме (по умолчанию)
#  'w' открыть для записи, содержимое файла удаляется, если файла нет создается новый
#  'a' открыть для дозаписи в конец файла, если файла нет ,создается новый
#  'b' открыть в бинарном режиме
#  '+' открыть для чтения и записи 'r+', 'w+', 'a+'

# open - встроенная функция


# r=open('text.txt', 'w',encoding='utf-8')
# r.write('Строка текста') # записать
# r.close # закрываем файл

# r=open('text_files.txt', 'w',encoding='utf-8')
# r.write('Строка текста') # записать
# r.close # закрываем файл

# r= open('text.txt')
# u= r.read() # прочитать
# print(u)
# r.close
'''

#работает грузит долго
# import os

# list_paths = []

# for adress, papka, file in os.walk('C:\\'):
#     for i in file:
#         full_path = os.path.join(adress, i)
#         list_paths.append(full_path) 



# r = open('text_files.txt', 'w', encoding='utf-8')
# for x in list_paths:
#     r.write(x + '\n')

# r.close()

'''
работа с файлом:
прочитать переменную - весь файл целиком? по строчно

r= open('text_files.txt')
for i in r:
    if 'print.exe' in i:
        print(i) # C:\Windows\System32\print.exe
    
r.close
'''


# бинарный режим работы: позволяет читать и записывать бинарные файлы

# r=open('WerFaultSecure.exe', 'rb') # указываем необходимый файл
# y=open('копия WerFaultSecure.exe', 'wb')

# while True:
#     var = r.read(1048576)
#     print(var.__sizeof__())
#     if var.__sizeof__() == # какое число уход в цикл, для завершения работы
#     break
#     y.write(var)

# print('Контрол')
# r.close()
# y.close()

'''
кодировка
'''

# r= open('text_new.txt', 'w', encoding='utf-8') # encoding='utf-8' самая распространенная кодировка
# r.write('строка текста')
# #print(r)
# r.close

# h = open('text_new.txt')# если не указать кодировку -  СЃС‚СЂРѕРєР° С‚РµРєСЃС‚Р°
h = open('text_new.txt', encoding='utf-8') # строка текста
print(h.read())   