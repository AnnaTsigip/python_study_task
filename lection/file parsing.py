# функция walk -  позволяет сгенерировать пути к файлам. #функция генератор за каждое обращение к ней она будет выдавать перечень значений

import os # модуль по работе с операционной системой
for i in os.walk('C:\\Users\User\Desktop\для задания'):
    print(i)
    break
