# Найти расстояние между точками в пространстве 2D/3D


x1 = float(input('введите координаты точки x_1: '))
x2= float(input('введите координаты точки x_2: '))
y1 = float(input('Введите координаты точки y_1: '))
y2 = float(input('Введите координаты точки y_2: '))
z1 = float(input('Введите кординаты точки z_1: '))
z2 = float(input('Введите кординаты точки z_2: '))
dx = x2 - x1
dy = y2 - y1
dz = z2 - z1
# print(X)
# print(Y)
# print(Z)

print(f'Расстояние между двумя точками равно {round((dx**2 + dy**2)**0.5, 2)}')
print(f'Расстояние между тремя точками равно {round((dx**2 + dy**2 + dz**2)** 0.5, 2)}')
