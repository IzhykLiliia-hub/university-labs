a = {"x": 1, "y": 2, "z": 3}
b = {"w": 10, "x": 11, "y": 2}

unique_keys = []
for key in a:
  if key not in b:
    unique_keys.append(key)

print(" ".join(unique_keys))