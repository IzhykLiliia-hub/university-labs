num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))
num3 = int(input("Введіть третє число: "))
remainder_12 = num1 % num2
remainder_13 = num1 % num3
is_divisible = (remainder_12 == 0)

print("=" * 50)
print(f"{'ЗВІТ АНАЛІЗУ ЗАЛИШКІВ':^50}")
print("=" * 50)
print(f"{'Перше число:':<32}{num1:>15}")
print(f"{'Друге число:':<32}{num2:>15}")
print(f"{'Третє число:':<32}{num3:>15}")
print("-" * 50)
print(f"{'Залишок:':<32}{remainder_12:>15}")
print(f"{'Залишок:':<32}{remainder_13:>15}")
print(f"{'Ділиться націло:':<32}{str(is_divisible):>15}")
print("=" * 50)