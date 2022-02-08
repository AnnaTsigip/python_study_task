#Найти максимальное из трех чисел

print('Введите a')
a = int(input())
print('Введите b')
b = int(input())
print('Введите c')
c = int(input())
max = a
if b > max:
    max =b
if c > max:
    max = c
print(f'максимальное число = {max}')