# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


print("X    Y   Z        ANSWER")
def pred(x, y, z):
    print(f"{x}   {y}   {z}    =    {(not (x or y or z)) == (not x and not y and not z)}")
    return (not (x or y or z)) == (not x and not y and not z)
if (pred(0, 0, 0) and pred(0, 0, 1) and pred(0, 1, 0) and
pred(0, 1, 1) and pred(1, 0, 0) and pred(1, 0, 1) and
pred(1, 1, 0) and pred(1, 1, 1)):
    print("True")
else:
    print("False")