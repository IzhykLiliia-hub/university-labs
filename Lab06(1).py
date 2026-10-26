diya = input().strip()

if "+" in diya:
  a, b = diya.split("+")
  print(int(a) + int(b))
elif "-" in diya:
  a, b = diya.split("-")
  print(int(a) - int(b))
elif "*" in diya:
  a, b = diya.split("*")
  print(int(a) * int(b))