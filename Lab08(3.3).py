numbers = input("Введіть послідовність чисел через пропуск: ").split()

stats = {i: 0 for i in range(1, 10)}

for num_str in numbers:
  num = int(num_str)
  if num == 0:
    break
  if 1 <= num <= 9:
    stats[num] += 1

result_list = [str(stats[i]) for i in range(1, 10)]
print(" ".join(result_list))