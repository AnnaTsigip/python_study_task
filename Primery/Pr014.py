# Найти третью цифру числа или сообщить, что её нет

a = int(input('Введите число для проверки a: '))
if a < 100:
    print('третьей цифры нет')
elif  1000 > a > 100:
    print(f'третья цифра: {a % 10}')
elif a > 999:
    print(f'{(a % 100) //10}')

