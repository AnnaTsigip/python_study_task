# Написать программу вычисления произведения чисел от 1 до N

N = int(input('N = '))
multi = 1
for i in range(1, N+1):
    multi = multi * i
print(f'Произведение чисел от 1 до {N} = {multi}')
