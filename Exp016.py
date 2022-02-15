# Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму


list = []
n = 5
count = 0
for i in range(1, n):
    list.append((1 + (1/i))**i)
    count += list[i-1]

print(list)
print(count)


