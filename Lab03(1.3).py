k = int(input())
day_of_week = (k - 1) % 7 + 1

if day_of_week >= 6:
  print("day off")
else:
  print("working day")