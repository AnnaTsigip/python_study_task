# Написать программу получающую набор 
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

list = []
N = int(input('Введите N: '))
num = 1
product = 1
for i in range(1, N+1):
    num = num * i
    product = num
    list.append(product)
print(list)

