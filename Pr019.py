# Определить номер четверти плоскости, в которой находится точка с координатами Х и У, причем X ≠ 0 и Y ≠ 0

X = int(input('Введите координаты точки X: '))
Y = int(input('Введите коорлинаты точки Y: '))
if X > 0:
    if Y > 0:
        print(f'координаты {X, Y} находится в первой четверти координат')
elif X < 0:
    if Y > 0:
        print(f'координаты {X, Y} находится во второй четверти координат')
elif X < 0:
    if Y < 0:
        print(f'координаты {X, Y} находится в третьей четверти координат')
elif X > 0:
    if Y > 0:
        print(f'координаты {X, Y} находится во второй четверти координат')
else:
    print('другие варианты?')
# а если одна из координат = 0?