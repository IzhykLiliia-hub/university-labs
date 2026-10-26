text = input().strip()
if text == "":
  words_count_split = 0
else:
  words_count_split = len(text.split())

print(f"Кількість слів: {words_count_split}")