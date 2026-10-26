n = int(input())

if n <= 1:
  print(0)
else:
  weighings = 0
  current = n
  while current > 1:
    current = (current + 2) // 3
    weighings += 1
  print(weighings)