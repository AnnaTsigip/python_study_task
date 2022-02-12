#Определить количество цифр в числе
number = int(input('введите число: '))
count = 0
while number > 0:
    number= number // 10
    count += 1 
print(f'в заданном числе {count} цифр')
