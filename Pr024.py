#Найти кубы чисел от 1 до N

N = int(input('N = '))
for i in range(1, N+1):
    print(f'{i} ^ 3 = {i**3}')
    #print(pow(i,3))
