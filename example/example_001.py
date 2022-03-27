# 1.По двум заданным числам проверить является ли одно квадратом второго 

first_number = int(input('Первое число: '))
second_number = int(input('Второе число: '))
if second_number == first_number**2:
    print(f'{second_number} является квадратом {first_number}')
else:
    print(f'{second_number} НЕ является квадратом {first_number}')