ip = input().strip()
parts = ip.split(".")
ok = len(parts) == 4

for p in parts:
  if not p.isdigit() or not (0 <= int(p) <= 255):
    ok = False
    break
  if len(p) > 1 and p[0] == "0":
    ok = False
    break

print("Yes" if ok else "No")