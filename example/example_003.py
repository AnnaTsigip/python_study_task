#3. Вывести на экран числа от -N до N

N = int(input('введите N: '))
count = int(-N)

while (count < N+1):

  print(count,end=' ')
  count+=1

 # с использованием модуля числа, если ввели отрицательное

Вывести на экран числа от -N до N

N = abs(int(input()))
for i in range(-N, N + 1):
    print(i, end = ' ')
