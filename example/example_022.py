# Найти сумму чисел списка стоящих на нечетной позиции



list = [1,3,1,4,5,6,7,8,1,2]
sum = 0
for i in range(0,len(list)):
    if list[i] % 2 != 0:
        sum += list[i]
print(sum)



