# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

X = int(input('Введите число Х '))
Y = int(input('Введите число Y '))
Z = int(input('Введите число Z '))

if not (X or Y or Z) == (not X and not Y ) and not Z:
    print(True)
else:
    print(False)

