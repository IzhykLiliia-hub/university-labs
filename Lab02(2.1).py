number = int(input("Введіть ціле трицифрове число: "))
hundreds = number // 100
tens = (number // 10) % 10
units = number % 10

reverse_number = units * 100 + tens * 10 + hundreds

print("=" * 45)
print(f"{'ТАБЛИЧНИЙ ЗВІТ РОЗБИТТЯ ЧИСЛА':^45}")
print("=" * 45)
print(f"{'Початкове число':<25} | {number:>15}")
print(f"{'Сотні':<25} | {hundreds:>15}")
print(f"{'Десятки':<25} | {tens:>15}")
print(f"{'Одиниці':<25} | {units:>15}")
print(f"{'Перевернуте число':<25} | {reverse_number:>15}")
print("=" * 45)