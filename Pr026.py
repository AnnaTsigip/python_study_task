# Возведите число А в натуральную степень B используя цикл

A = int(input('введите число A: '))
B = int(input('Введите B:'))
C = 1
for i in range (1, B+1):
    C = C * A
print(C)