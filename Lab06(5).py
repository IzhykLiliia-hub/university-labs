x = 0
y = 0

while True:
  line = input().strip()
  if line == "Treasure!" or line == "":
    break

  parts = line.split()
  direction = parts[0]
  steps = int(parts[1])

  if direction == "North":
    y += steps
  elif direction == "South":
    y -= steps
  elif direction == "East":
    x += steps
  elif direction == "West":
    x -= steps

print(f"Кінцеві координати: X = {x}, Y = {y}")