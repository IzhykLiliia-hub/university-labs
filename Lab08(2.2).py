capitals = {
    "China": "Beijing",
    "Denmark": "Copenhagen",
    "Ukraine": "Kyiv",
    "Canada": "Ottawa",
    "France": "Paris",
}

sorted_capitals_desc = sorted(
    capitals.items(), key=lambda item: item[1], reverse=True)
print(sorted_capitals_desc)