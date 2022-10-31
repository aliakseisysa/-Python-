#1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

#Пример:

#- 6782 -> 23
#- 0,56 -> 11

num = input('Enter any float number: ')

my_list = num.split(".")

if len(my_list) > 1:
    num = my_list.pop(1)
else:
    num = num

if len(num) == 1:
    print(num)

else:

    my_list = [int(i) for i in num]

    my_sum = my_list[0] + my_list[1]
    for i in range(2,len(my_list)):
        my_sum = my_sum + my_list[i]

    print(my_sum)

#2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

#Пример:

#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

my_num = int(input('Enter any integer number: '))

my_list_h = [i for i in range(1,my_num+1)]

my_list_f = []
my_list_f.extend(my_list_h[0:2])
my_mult= my_list_f[0] * my_list_f[1]
for i in range(2, len(my_list_h)):
    my_mult = my_mult * my_list_h[i]
    my_list_f.append(my_mult)

print(my_list_f)

#3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

#Пример:

#- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

#4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
#Реализуйте алгоритм перемешивания списка.

my_num = int(input('Enter any integer number: '))
import random

array = [random.randint(-my_num,my_num) for _ in range(my_num)]

print(array)