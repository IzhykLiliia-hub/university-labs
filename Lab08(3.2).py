text = input("Введіть текст: ").split()
word_freq = {}

for word in text:
  word_freq[word] = word_freq.get(word, 0) + 1
sorted_words = sorted(word_freq.items(), key=lambda item: item[0], reverse=True)

for word, freq in sorted_words:
  print(f"{word}: {freq}")