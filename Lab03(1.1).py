hours = int(input())
rate = float(input())

if hours > 40:
  total_pay = 40 * rate + (hours - 40) * (rate * 1.5)
else:
  total_pay = hours * rate

print(f"{total_pay:.2f}")