#Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#  *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

k = 3
from cgitb import text
from random import randint
lst = [randint(0, 100) for i in range(k+1)]
print(lst)

lst2 = []
for i in range (len(lst)):
    lst2.append(str(lst2[i]) + '*x ^ ' + str(k - i) + ' + ')

#print(lst2)
lst2.pop
lst2.append(str(lst2[-1]))
lst2.append(' = 0')
text = ' '.join(lst2)

with open(file.txt, 'w', encoding='utf-8') as f:
    f.write(text)

