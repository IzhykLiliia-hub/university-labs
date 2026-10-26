capitals = {
    "China": "Beijing",
    "Denmark": "Copenhagen",
    "Ukraine": "Kyiv",
    "Canada": "Ottawa",
    "France": "Paris",
}
sorted_capitals = sorted(capitals.items(), key=lambda item: item[1])
print(sorted_capitals)