n = int(input())
for i in range(3, n + 1):
  row = ""
  for j in range(i, n + 1):
    row += str(j)
  print(row)