# 14.Подсчитать сумму цифр в вещественном числе


num = float(input('numner = ')) # вводим число
num_str = str(float(num)) # переводим в строку
#print(type(num_str)) 
num_str1 = num_str.split('.') # разбиваем по разделителю
# print(num_str1)
num1 = int(num_str1[0]) # записываем до запятой
num2 = int(num_str1[-1]) # после запятой
#print(num1)
#print(num2)

def sum_num(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return(sum)

print(sum_num(num1) + sum_num(num2))
#print(sum_num(num2))


