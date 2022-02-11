# Подсчитать сумму цифр в числе

a = int(input("Введите целое: "))
summary = 0
while (a != 0):
    summary = summary + a % 10
    a = a // 10
print("Сумма цифр числа равна: ", summary)
