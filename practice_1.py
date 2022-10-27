# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

###Допустим, что пользователь вводит числа от 1 до 7, проверку на ввод других чисел не проводим.

a = int(input("Enter the week's day number: "))

if a <= 5:
    print("no")
else:
    print("yes")

# 2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in [True,False]:
    for y in [True,False]:
        for z in [True,False]:
            if not (x or y or z) is not x and not y and not z:
                print("true")


# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x = float(input("Enter the first coordinate of a point: "))
y = float(input("Enter the second coordinate of a point: "))

if x > 0 and y > 0:
    print("I quarter")
elif x > 0 and y < 0:
    print("IV quarter")
elif x < 0 and y > 0:
    print("II quarter")
else:
    print("III quarter")


# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек
# в этой четверти (x и y).

qt = int(input("Enter the number of the quarter: "))

if qt == 1:
    print("Possible x range is (0; infinity), possible y range is (0; infinity)")
elif qt == 2:
    print("Possible x range is (- infinity; 0), possible y range is (0; infinity)")
elif qt == 3:
    print("Possible x range is (- infinity; 0), possible y range is (- infinity; 0)")
else:
    print("Possible x range is (0; infinity), possible y range is (- infinity; 0)")


# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними
# в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

ax = float(input("Enter the first coordinate of A: "))
ay = float(input("Enter the second coordinate of A: "))

print(f"A({ax, ay})")

bx = float(input("Enter the first coordinate of B: "))
by = float(input("Enter the second coordinate of B: "))

print(f"B({bx, by})")

ED = ((bx-ax)**2+(by-ay)**2)**0.5

print(f"The distance between A and B is equal to {ED}.")