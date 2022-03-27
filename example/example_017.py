# Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt   в одной строке одно число
list = []
N = int(input('Введите N: '))
for i in range(-N, N+1):
    list.append(i)
#print(list)

multi = 1
for i in range(-N, N):
     if i!=0:
         multi = multi * i
print(f'Произведение чисел = {multi}')

f1 = ""
for i in list:
    f1 += str(i)+ " " 

new_file = open('file_Exp017.txt', 'a')
new_file.write(f1)
new_file.close()

