x=set(input("Введіть слово для створення множин: ").lower())
words=input("Введіть слова: ").lower().split()
for word in words:
    if set(word).issubset(x):
        print(word)
