numbers=list(map(int,input("Введіть цілі числа: ").split()))
result=sorted(set(numbers))
print("Результат: ",result)