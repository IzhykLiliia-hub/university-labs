text=input("Введіть рядок: ")
symbols={}
for char in text:
    symbols[char]=symbols.get(char,0)+1
for char,count in symbols.items():
    print(char,"-",count)