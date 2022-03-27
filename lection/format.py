# форматирование строк

# самый старый вариант %s :
# enter = input('Your name:')
# s = 'Hello %s, I am %s'% (enter, 'Python')
# print(s)  # Hello Anna, I am Python
 


# # второй вариант .format в {} можно указывать порядок выведения 
# enter = input('Your name:')
# s1 = 'Hello {}, I am {}'.format(enter, 'Python')  # #Hello Anna, I am Python
# s1 = 'Hello {1}, I am {0}'.format(enter, 'Python')  # Hello Python, I am Anna
# print(s1) 


# новый вариант f:
#в выводе можно сразу проводить операции,  использовать функции/методы.

enter = input('Your name: ')
var = 'stroka'

#сложим 2+2
s2 = f'Hello {enter}, I can do it in f-string {2+2}' # Hello Anna, I can do it in f-string 4

#посчитаем длину переменной var
s2 = f'Hello {enter}, I can do it in f-string {len(var)}'  # Hello Anna, I can do it in f-string 6
print(s2)

