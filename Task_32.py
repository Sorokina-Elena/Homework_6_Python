'''
Задача 32: Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)
'''

list = input("Введите список: ").split()
print(list)
min = int(input("Введите минимальное число диапазона: "))
max = int(input("Введите максимальное число диапазона: "))
for i in range(len(list)):
    if int(list[i]) >= min and int(list[i]) <= max:
        print(i)