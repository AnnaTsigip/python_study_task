#20. Определить, присутствует ли в заданном списке строк, некоторое число 

string = ['33коровы', '3друга', '10строк']
n = input('Какое число ищем? ')
for i in range(len(string)):
    if str(n) in string[i]:
        print(f'{n} есть в строке на позиции {string[i]}')
else:
    print(f'{n} в строке нет')
        


