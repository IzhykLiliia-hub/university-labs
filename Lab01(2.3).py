total_seconds = int(input("Введіть загальну кількість секунд: "))

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"{hours} годин : {minutes} хвилин : {seconds} секунд")