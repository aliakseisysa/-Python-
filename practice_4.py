# 1. Вычислить число c заданной точностью d
#
# Пример:
#
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import random
d = random.randint(-10, -1)

def pi():
    pi = 0
    n = 4
    p = 1
    for i in range(1,10000000):
        a = 2*(i%2)-1
        pi += a*n/p
        p += 2
    return(pi)

print(f"Accuracy is set to {10**d}")
num = pi()
print(f"Rounded pi value is {round(num, -d)}")

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

##Сначала определим все простые числа до N с использованием алгоритма Эратосфена
def sieve(n):
    _sieve = [i for i in range(n)]
    _sieve[1] = 0

    for i in range(2, n):

        if _sieve[i] != 0:
            j = i * 2

            while j < n:
                _sieve[j] = 0
                j += i

    result = [i for i in _sieve if i != 0]

    return result

my_num = int(input('Enter any positive integer number: '))

sieve_nums = sieve(my_num+1)

##Далее определяем все простые множители числа N

nat_mult = []

while True:

    for el in sieve_nums:
        if my_num % el == 0:
            nat_mult.append(el)

    break

print(my_num, sieve_nums, nat_mult)


# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.

import random
array = [random.randint(-10,10) for _ in range(40)]
print(array)

def uniq_nums(array):

    array.sort()
    new_array = []
    new_array.append(array[0])

    for i in range(1,len(array)):
        if array[i] == array[i-1]:
            i += 1
        else:
            new_array.append(array[i])

    return new_array

print(uniq_nums(array))

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
#
# Пример:
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

k = int(input('Enter k: '))
i = 0

import random

koeff = []

while True:

    if i <= k:
        koef = random.randint(0,101)
        koeff.append(koef)
        i += 1
    else:
        break

print(koeff)

levels = []

for i in range(k,-1,-1):
    levels.append(i)

print(levels)

expression = []

for i,j in zip(koeff, levels):
    expression.append(f"{i}*x^{j}")

polynom = '+'.join(expression)

print(f'{polynom} = 0')

f = open("polynom.txt", "a")
f.write(f'{polynom} = 0')
f.close()