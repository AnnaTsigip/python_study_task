# Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.


subsequence = []
count = int(input('Введите количество членов последовательности: '))
for i in range(count):
    if i % 2 == 0:
        subsequence.append(3**i)
    else:
        subsequence.append(3**i * -1)
print(subsequence)


# def create_list(n):
#     lst = []
#     spam = 1
#     for i in range(n):
#         lst.append(spam)
#         spam = spam *-3
#         return lst

# print(create_list(5))