# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

my_list = input('Enter several numbers separeted by spaces: ').split(' ')
my_list2 = list(map(int,(my_list)))
print(my_list2)

sum = 0
for i in range (len(my_list2)):
    if i % 2 != 0:
        sum += my_list2[i]
print(sum)



