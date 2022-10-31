# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
# Пример:
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

my_list = [2, 3, 5, 9, 3]

array_odd = []

for i in range(len(my_list)):
    if i%2!=0:
        odd_num = my_list[i]
        array_odd.append(odd_num)

my_sum = array_odd[0]
for i in range(1,len(array_odd)):
    my_sum = my_sum + array_odd[i]

print(array_odd, my_sum)

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

my_list = [2, 3, 4, 8, 1, 5, 6]

if len(my_list)%2==0:
    new_list = []
    for i in range(int(len(my_list)/2)):
        my_mult = my_list[0+i]*my_list[-1-i]
        new_list.append(my_mult)
    print(new_list)
else:
    dup_num = my_list[int(len(my_list)//2)]
    my_list.insert(int(len(my_list)//2),dup_num)
    new_list = []
    for i in range(int(len(my_list)/2)):
        my_mult = my_list[0+i]*my_list[-1-i]
        new_list.append(my_mult)
    print(new_list)

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_array = [1.1, 1.2, 3.1, 5, 10.01]

new_array = []
for el in my_array:
    el = el%1
    new_array.append(el)

max_new_array = new_array[0]

for i in range(1,len(new_array)):
    if new_array[i]>max_new_array:
        max_new_array = new_array[i]

min_new_array = new_array[0]

for i in range(1,len(new_array)):
    if new_array[i]<min_new_array:
        min_new_array = new_array[i]

print(max_new_array - min_new_array)

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

dec_num = int(input('Enter any decimal number: '))

bin_num = []

while True:
  if dec_num//2 > 1:
    bin_num.append(dec_num%2)
    dec_num = dec_num//2
  else:
    bin_num.append(dec_num%2)
    bin_num.append(dec_num//2)
    bin_num.reverse()
    s = [str(i) for i in bin_num]
    break

print("".join(s))

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов

def fib_dict(n):
    fib_d = {0: 0, 1: 1}

    def _fib_dict(n):
        if n in fib_d:
            return fib_d[n]

        fib_d[n] = _fib_dict(n - 1) + _fib_dict(n - 2)
        return fib_d[n]

    return _fib_dict(n)

new_num = int(input('Enter any integer number: '))
fib_list = [fib_dict(el) for el in range(new_num+1)]
adj_fib_list = []
for el in fib_list:
    adj_fib_list.append(el*(-1))

fib_list.extend(adj_fib_list)
fib_list.sort()

print(fib_list)