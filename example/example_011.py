# Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

list = []
n = 5
for i in range(n):
    if i % 2 == 0:
        list.append(3**i)
    else:
        list.append(3**i * -1)
print(list)



# def create_list(n):
#     lst = []
#     spam = 1
#     for i in range(n):
#         lst.append(spam)
#         spam = spam *-3
#         return lst

# print(create_list(5))