text = input("Введіть рівно два слова через пропуск: ")
space_index = text.find(" ")
first_word = text[:space_index]
second_word = text[space_index + 1 :]
print(f"{second_word} {first_word}")