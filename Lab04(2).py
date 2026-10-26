poem = """Yes, I'll smile, indeed, through tears and weeping
    Sing my songs where evil holds its sway,
    Hopeless, a steadfast hope forever keeping,
    I shall live! You thoughts of grief, away!"""

# 1
print("Перші 16 символів:", poem[:16])

# 2
print("Загальна кількість символів:", len(poem))

# 3
print("Починається з 'Yes':", poem.startswith("Yes"))

# 4
print("Закінчується на 'I shall live!':", poem.endswith("I shall live!"))

# 5
print("Індекс першої коми:", poem.find(","))
print("Індекс останньої коми:", poem.rfind(","))
print("Загальна кількість ком:", poem.count(","))

# 6
print("Всі символи alnum:", poem.isalnum())