s = input().strip()
encoded = ""
count = 1

for i in range(len(s) - 1):
  if s[i] == s[i + 1]:
    count += 1
  else:
    encoded += (str(count) if count > 1 else "") + s[i]
    count = 1

if s:
  encoded += (str(count) if count > 1 else "") + s[-1]

print(encoded)