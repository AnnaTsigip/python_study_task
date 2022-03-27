# Дано число из отрезка [10, 99]. Показать наибольшую цифру числа

# import random
# list = [random.randint(10, 99)]
# print(list)

a = int(input('Введите число от 10 до 99: '))
b = a % 10
c = a // 10
if b > c:
    print(f'в числе {a} наибольшая цифра {b}')
elif b == c:
    print(f'в числе {a} цифры {b} = {c}')
else:
    print(f'в числе {a} наибольшая цифра {c}')