city_to_country = {
    "Seattle": "USA",
    "New York": "USA",
    "Kyiv": "Ukraine",
    "Paris": "France",
    "Ottawa": "Canada",
}
city = input("Введіть назву міста: ").strip()
if city in city_to_country:
  print(city_to_country[city])
else:
  print("Місто не знайдено")