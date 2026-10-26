mountains = {
    "Hoverla": 2061,
    "Brebenescul": 2032,
    "Pip Ivan Chernogirsky": 2028,
    "Rebra": 2001,
    "Menul": 1998,
    "Turkul": 1933,
    "Gutyn Tomnatyk": 2016,
    "Petros": 2020,
    "Rebra": 2001,
    "Smotrych": 1898,
}

top_3 = sorted(mountains.items(), key=lambda item: item[1], reverse=True)[:3]

for name, height in top_3:
  print(f"{name}: {height} m")