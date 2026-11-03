L=set(input("Введіть елементи: ").split())
A=set(map(input("Введіть числа множини А: ").split()))
B=set(map(input("Введіть числа множини В: ").split()))


print("Обєднання A та B:",A|B)
print("Перетин A та B:",A&B)
print("Різниця A та B:",B-A)
print("Різниця B та A:",A-B)
print("Доповнення A:",U-A)
print("Доповнення B:",U-B)
