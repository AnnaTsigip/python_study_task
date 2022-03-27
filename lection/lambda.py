# def some(x):
#     return x/5

# print(some(7))

# var = lambda x: x/5
# print(var(7))

"""
пример применения
"""
list_of = [['Adam', 29], ['Jonny', 3*1/12], ['Jess', 25]]

#отсортировать по возрасту:

def s(x):
    return x[1]

r= sorted(list_of, key=s)
print(r) # [['Jonny', 0.25], ['Jess', 25], ['Adam', 29]]

# lanbda

r=sorted(list_of, key = lambda x: x[1])
print(r) # [['Jonny', 0.25], ['Jess', 25], ['Adam', 29]]


#функция filter 

x= list(filter(lambda x: x[1] > 18, list_of))
print(x) # [['Adam', 29], ['Jess', 25]]