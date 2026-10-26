item_name = input("Введіть назву товару: ")
price = float(input("Введіть ціну за одиницю (грн): "))
quantity = int(input("Введіть кількість (шт): "))

total_cost = price * quantity
print("\n--- ЧЕК ПОКУПКИ ---")
print(f"Товар:    {item_name}")
print(f"Ціна:     {price:8.2f} грн")
print(f"Кількість:{quantity:8d} шт")
print("-" * 21)
print(f"Загалом:  {total_cost:8.2f} грн")