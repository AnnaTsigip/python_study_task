

# if True: #выполняется первое условие if
#     print('if')
# elif True:
#     print('elif')
# else:
#     print('else')


# if False:
#     print('if')
# elif True: # если If - False, будет выполняться elif 
#     print('elif')
# else:
#     print('else')

# if False:
#     print('if')
# elif False:  
#     print('elif')
# else: # если if и elif - False, будет выполняться else
#     print('else')


#операторы сравнения: задачи
#логические операции
# >, >=, <, <=, ==, !=
# not, and, or, не путать с &, |, ^
# и еще: is, is not, in, not in

# при помощи логических операций можно обезопасить код от ошибок:
# x = -3

# if x == 0:
#     print('if')
# elif x > 0:
#     print('elif')
# else: 
#     print('else')



# x = 0

# if x == 0:
#     x+= 1

# print(5/x)


# x = [1,2]

# if x == 0:
#     x = 1
#     print('x был равен нулю')
# elif type(x) == type(5) or type(x) == type(5.5):
#     print('x допустимое значение')
# else:
#     print('в x недопустимый тип данный')
#     x = 1


# print(100/x)



#оператор in проверяет есть ли последовательность в полследовательности?

#'www' in 'www.youtube.com' если есть - True нет - False

# модуль os - стандартной библиотеки, 
# обеспечивает взаимодействие с операционной системой

# метод system 


# import os

# sayt = input('Ввод сайта: ')

# if 'https://' in sayt:
#     os.system('start ' + sayt)
#     print('if')

# elif 'www.' in sayt:
#     sayt = 'https://' + sayt
#     os.system('start ' + sayt)
#     print('elif')

# else:
#     sayt = 'https://www.' + sayt
#     os.system('start ' + sayt)
#     print('else')


# модуль os и модуль time
# import os
# import time

# os.system ('start https://www.youtube.com')

# time.sleep(5) # задержка в открытии следующего файла/программы

# os.startfile('C:\\Program Files (x86)\Skrinshoter')
'''
while - выполняет код, пока условие True

x = 0

while x < 5:
    x +=1
    print(x)

else:
    print(x)

# Факториал:

while True: #можно сделать программу бесконечной, т.е. после просчета, сразу просит новое число без нового запуска: 
    x = int(input('Введите число: '))
    count = 0
    y = 1

    while count < x:
        count += 1
        y *= count

    else:
         print(y)


# continue 


# без доп. условий, у цикла количество сработок по длине строки len(x)
x = ''


while len(x) < 5:
    y = input('Ввод данных: ')
    x += y
else:
    print(x)

# continue 

x = ''


while len(x) < 5:
    y = input('Ввод данных: ')
    if y == 'o':
        continue# т.е прервется сработка цикла, код x+=y не сразртает, но цикл продолжится пока не выполнится условие count < 5, 
                  #т.е. 'o' будет пропускаться, и цикл будет заправшивать элементы пока не введется другая буква
    x += y
else:
    print(x)

#break

x = ''


while len(x) < 5:
    y = input('Ввод данных: ')
    if y == 'l':
        break # т.е. цикл вообще прервется и else не выполнится, но программа работает дальше
    x += y
else:
    print(x)
print(x) # продолжает работать то что за циклом


 
import os

while True:
    sayt = input('Ввод сайта\n')
    if sayt == 'stop':
        break

    if 'https://' in sayt:
        os.system('start ' + sayt)
        print('if')

    elif 'www.' in sayt:
        sayt = 'https://' + sayt
        os.system('start ' + sayt)
        print('elif')

    else:
        sayt = 'https://www.' + sayt
        os.system('start ' + sayt)
        print('else')
'''

# for
#1:
# for i in 'stroka text': 
#     print(i)

# print('программа работает дальше')

# #2: 
# m = 'stroka text'
# for i in m: 
#     print(i)

# print('программа работает дальше')

# 1 и 2 результат аналогичен

#3: с доп. проверкой на содердание букв, и остановкой цикла

# m = 'stroka text'
# count = 0
# for i in m: 
#     if i == 't':
#         print('В строке есть буква t')
#         count +=1
#     if i == 'a':
#         break

# else:
#     print(f'Цикл завершен, букв t {count}')

# print('программа работает дальше')


#4 c continue - пропускает букву, выводит строку без пропущенной буквы

# m = 'stroka text'
# count = 0
# for i in m: 
#     if i == 't':
#         continue
#         print('В строке есть буква t')
#         count +=1
#     print(i)
   
# else:
#     print(f'Цикл завершен, букв t {count}')

# print('программа работает дальше')

'''
цикл в цикле
проверка какое количество букв в строке введеной пользоователем

x = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
y = input('Введите строку\n')

for i in x:
    count = 0
    for r in y:
        if i == r:
            count += 1
    if count > 0:
        print(f'букв {i} было {count}')

'''

#for + встроенная функция range, которая генерирует последовательность чисел


# for x in range (start, stop, step): #в функции range  3 параметра старт, стоп, шаг, в зависимости от того какие из них записывать вывод будет разный
#     print(x)

# for x in range (10): # если только стоп, то по умолчанию от 0 до стоп
#     print(x)

# for x in range (5, 10): # если старт и стоп, то от старт до стоп
#     print(x)

# for x in range (1, 10, 2): # если старт, стоп и шаг, то от старт до стоп с шагом
#     print(x)

for x in range (10, -10, -2): # может генерить в обратной порядке
     print(x)