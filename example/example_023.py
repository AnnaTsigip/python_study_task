#Найти произведение пар чисел в списке.
#Парой считаем первый и последний элемент, второй и предпоследний и т.д. Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]


# for i, item in enumerate(list):
#     list[i] = int(item)
# print(type(list))


list = [2,3,8,9,4,6,2,9,3]
list2 = list[::-1] # переворачиваем список
list3 = []
print(list2)
for i in range(0,len(list)//2):
    list3.append(list[i]*list2[i])       
      
print(list3)



# # Объявляем пустой список
# enter = list()

# # Ввод данных
# # Просим ввести количество элементов в списке и записываем число в переменную n
# n = int(input('Количество элементов '))
# # Запускаем цикл на n раз
# for i in range(n):
#         # Принимаем в консоли значение элемента, приводим его к целому типу
#     elem = int(input())
#     # Добавляем элемент в список
#     enter.append(elem)
# print(elem)

# prodact = 1 # Счетчик подошедших по условию пар
# # Получаем индексы элементов списка от 0 до предпоследнего в цикле
# for i in range(n - 1):
#     for j in range(n -1):
#         if enter[i] < n//2 and enter[j]< n//2:

#             prodact = enter[i] * enter[j]
#             print(prodact)