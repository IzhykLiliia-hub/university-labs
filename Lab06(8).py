text = input()
digits = []

for char in text:
  if char.isdigit():
    digits.append(char)

if not digits:
  print(0)
else:
  digits.sort(reverse=True)
  if digits[0] == "0":
    print(0)
  else:
    print("".join(digits))