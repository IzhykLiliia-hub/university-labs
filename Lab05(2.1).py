s = int(input())
total_money = 0
gift = 0
n = 0

while total_money < s:
  n += 1
  if n == 1:
    gift = 1
  else:
    gift = gift * 2 + n
  total_money += gift

print(n)