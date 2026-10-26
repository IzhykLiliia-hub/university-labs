import math

a = float(input("Введіть сторону a: "))
b = float(input("Введіть сторону b: "))
c = float(input("Введіть сторону c: "))

perimeter = a + b + c
p = perimeter / 2

area = math.sqrt(p * (p - a) * (p - b) * (p - c))

print("\n--- ГЕОМЕТРИЧНІ РОЗРАХУНКИ ---")
print(f"Сторони трикутника: a = {a}, b = {b}, c = {c}")
print(f"Периметр:           {perimeter:.2f}")
print(f"Площа:              {area:.2f}")