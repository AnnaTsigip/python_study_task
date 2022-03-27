#Программа проверяет пятизначное число на палиндромом

from unicodedata import digit


number = int(input('число для проверки: '))
copy_number = number
result = 0
while number!= 0:
    digit = number % 10
    result = result * 10 + digit
    number = number // 10
print(f'получили число: {result}')
if result == copy_number:
    print('число - палиндром')
else:
    print('число НЕ палиндром')








