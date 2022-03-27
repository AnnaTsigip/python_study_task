#обычная запись:

# def some():
#     list_text = []
#     with open('text_fg.txt', encoding='utf-8') as r:
#         for x in r:
#             list_text.append(x)
#     return list_text

# for i in some():
#     print(i.split())
#Вывод   
# ['строка', 'текста']
# ['с', 'какойто']
# ['информацией']


'''

через функцию генератор:

def some():
    with open('text_fg.txt', encoding='utf-8') as r:
        for x in r:
            yield x #  обозначение функции генератора

for i in some():
    print(i.split())

#вывод:
# ['строка', 'текста']
# ['с', 'какойто']
# ['информацией']
'''

# пример:

def some():
    with open('text_fg.txt', encoding='utf-8') as r:
        for x in r:
            yield x

p = some()
# print(next(p)) # строка текста
# print(next(p)) # с какойто
# print(next(p)) # информацией

for i in p:
    print(i) # в цикле выведутся сразу:
    # строка текста
    # с какойто
    # информацией