#В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. 
#Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# list = [1.1, 1.2, 3.1, 5, 10.01]
# list.

#точнее :

list_float = [1.1, 1.2, 3.1, 5, 10.02]
# min = 1
# max = -1
# for i in range(0, len(list)):
#     temp = list[i] - int(list[i])
#     if temp != 0:
#         if temp > max:
#             max = temp
#         elif temp < min:
#             min = temp
# print(round(max - min,5))

####2   - 
list_float = [1.1, 1.2, 3.1, 5, 10.02]
list = []
max_num = 0
min_num = 0
for i in list_float:
    list.append(round(i%1,2))
print(list)
max_num = (max(list))
min_num = (min(list))
print(max_num - min_num)