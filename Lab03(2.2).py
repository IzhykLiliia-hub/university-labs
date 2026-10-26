n = int(input())

if n % 10 != 0:
  print(-1)
else:
  c500 = n // 500
  n %= 500
  c200 = n // 200
  n %= 200
  c100 = n // 100
  n %= 100
  c50 = n // 50
  n %= 50
  c20 = n // 20
  n %= 20
  c10 = n // 10

  total_bills = c500 + c200 + c100 + c50 + c20 + c10
  print(total_bills)