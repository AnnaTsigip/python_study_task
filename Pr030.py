#Показать кубы чисел, заканчивающихся на четную цифру

a = int(input('Введите число: '))
for i in range(1, a+1):
    if i**3 % 2 == 0 and i**3%10 != 0:
        print(i**3)