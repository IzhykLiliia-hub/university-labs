# Завдання 1.3. Обчислення вартості книг
a = int(input("Введіть кількість гривень за 1 книгу: "))
b = int(input("Введіть кількість копійок за 1 книгу: "))
n = int(input("Введіть кількість книг (n): "))
total_hryvni = a * n
total_kopiyka = b * n

total_hryvni += total_kopiyka // 100
final_kopiyka = total_kopiyka % 100

print(f"Вихідні дані: {a} {b} {n}")
print(f"Вихідні дані: {total_hryvni} {final_kopiyka}")