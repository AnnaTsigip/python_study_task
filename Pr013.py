# Выяснить, кратно ли число заданному, если нет, вывести остаток

a = int(input('Введите число a: '))
b = int(input('кратно? введите b: '))
if (a % b == 0):
    print(f'{a} кратно {b}')
else:
    print(f'{a} НЕ кратно {b}, остаток: {a % b}')