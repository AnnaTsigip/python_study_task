# контексный менеджер

r=open('text_wuth_as.txt', 'a', encoding='utf-8')
try:
    r.write('something' + '\n')
    10/0 #- работа прерветя из-за ошибки
    r.write('что-то еще')
finally: # чтобы всегда закрылось
    r.close()

print('Все норм')


#with-as - самостоятельно открывает и закрывает файл close не нужен. при ошибке файл закрывается безопасно

# with open('text_wuth_as.txt', 'a', encoding='utf-8') as r:
#     r.write('something' + '\n')
#     10/0
#     r.write('что-то еще')
# print('Все норм')