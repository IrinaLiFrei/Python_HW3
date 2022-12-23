# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10
    

num = int(input('Enter any number: '))
my_list = []

while num:
    my_list.append(num % 2)
    num //= 2
my_list.reverse()
print("".join(str(i) for i in my_list))