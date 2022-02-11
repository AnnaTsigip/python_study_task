# Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y
x = [True, False]
y = [True, False]
for i in x:
    for j in y:
        print('Для x:', x[i])
        print('Для y:', y[j])
        if (not (x[i] or y[j]) == (not x[i] and not y[j])):
            print('Выражение истинно')
        else:
            print('Выражение ложно')