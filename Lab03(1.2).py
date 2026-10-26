number = int(input())

h = number // 100
t = (number // 10) % 10
u = number % 10

sum_digits = h + t + u
sum_cubes = h**3 + t**3 + u**3

if sum_digits**2 == sum_cubes:
  print(True)
else:
  print(False)