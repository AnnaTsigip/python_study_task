# 6. Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

day = int(input('Введите число дня недели: '))
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
if day >= 1 and day < 6:
    day_week = week[day-1]
    print(f'{day_week} - будний день')
elif day >5:
    day_week = week[day-1]
    print(f'{day_week} - выходной')
        
        

        # как обраблтать ошибку с числами больше 7