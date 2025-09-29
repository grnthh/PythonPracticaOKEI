a = int(input("введите размер коллекции: "))
collection = []
for i in range(a):
    value = input(f"введите значение {i+1}: ")
    collection.append(value)
print("результат:", collection)