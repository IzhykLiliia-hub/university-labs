# Завдання 2.2. Фінансовий калькулятор
principal = float(input("Введіть початкову суму вкладу (грн): "))
rate = float(input("Введіть річну процентну ставку (%): "))
months = int(input("Введіть термін укладання (місяців): "))

interest = (principal * rate * months) / (12 * 100)
total_amount = principal + interest

print("\n--- ФІНАНСОВИЙ ЧЕК ---")
print(f"Початковий вклад:  {principal:10.2f} грн")
print(f"Ставка річних:     {rate:10.1f} %")
print(f"Термін (місяців):  {months:10d}")
print("-" * 30)
print(f"Нараховані відсотки:{interest:9.2f} грн")
print(f"Загальна сума:     {total_amount:10.2f} грн")