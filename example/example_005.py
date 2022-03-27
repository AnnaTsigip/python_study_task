# 5. Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30

# 5 и 10
# num = int(input('Введите число: '))
# if num % 5 == 0 and num % 10 == 0:
#     print(f'{num} кратно 5 и 10') 
# else:
#     print(f'{num} НЕ кратно 5 и 10') 

# 15 но не 30:  например 15, 45,75
num = int(input('Введите число: '))
if num % 15 == 0 and not num % 30 == 0:
    print(True) #  print(f'{num} кратно 15 не кратно 30') 
else:
    print(False) 