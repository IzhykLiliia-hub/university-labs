n0 = 1000
r = 0.14
for year in range(1, 11):
  amount = n0 * (1 + r) ** year
  print(f"{amount:.2f}")