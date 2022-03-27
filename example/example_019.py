# Реализовать алгоритм задания случайных чисел. Без использования встроенного 
# генератора псевдослучайных чисел

# с генератором 
# from random import randrange

# n = 10
# a = [randrange(1, 10) for i in range(n)]
# print()

#без генератора, с использованием времени


def rand_numbers(start, stop):
    num = time.time() # проверить
    delta = stop - start
    rnd = float(str(num)[::-1][:3])/1000
    return round(rnd * delta)

print(rand_numbers(1, 20))