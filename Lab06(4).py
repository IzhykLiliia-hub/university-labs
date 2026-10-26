s = input().strip()
result = 0
curr = ""
sign = "+"

for char in s + "+":
  if char.isdigit():
    curr += char
  else:
    num = int(curr)
    if sign == "+":
      result += num
    else:
      result -= num
    sign = char
    curr = ""

print(result)