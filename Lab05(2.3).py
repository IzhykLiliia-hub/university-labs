k = int(input())
n = 0

while (n * (n + 1)) // 2 <= k:
  n += 1

print(n - 1)