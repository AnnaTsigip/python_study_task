# Найти максимальное из пяти чисел

print('Введите a')
a = int(input())
print('Введите b')
b = int(input())
print('Введите c')
c = int(input())
print('Введите d')
d = int(input())
print('Введите e')
e = int(input())
max = a
if b > max:
    max =b
if c > max:
    max = c
if d > max:
    max = d
if e > max:
    max = e
print(f'максимальное число = {max}')


