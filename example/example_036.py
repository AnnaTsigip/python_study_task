#Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую последовательность.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д

original_list = [1, 5, 2, 3, 4, 6, 1, 7]
new_list = []
max = original_list[0]
new_list.append(original_list[0])
for i in original_list:
    if i > max:
        max = i
        new_list.append(max)

print(new_list)