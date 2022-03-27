#Найти сумму чисел от 1 до А

A = int(input('A = '))
sum = 0
for i in range(1, A+1):
    sum = sum + i
print(sum)