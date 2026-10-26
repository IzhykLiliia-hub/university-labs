total_seconds = int(input("Введіть загальну кількість секунд: "))
minutes = total_seconds // 60
seconds = total_seconds % 60

print("=" * 35)
print(f"Час: {minutes:02d} хв : {seconds:02d} сек")
print("=" * 35)