number = int(input("Введіть ціле двоцифрове число: "))

tens = number // 10
units = number % 10
sum = tens + units

print("=" * 45)
print(f"{'АНАЛІЗ ДВОЦИФРОВОГО ЧИСЛА':^45}")
print("=" * 45)
print(f"{'Початкове число':<25} | {number:>15}")
print(f"{'Десятки':<25} | {tens:>15}")
print(f"{'Одиниці':<25} | {units:>15}")
print(f"{'Сума цифр':<25} | {sum:>15}")
print("=" * 45)