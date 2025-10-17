числа = []
while True:
    n = int(input("введите число: "))
    if n == 0:
        break
    числа.append(n)
среднее = sum(числа) / len(числа)
print(f"avg = {среднее}")
for x in числа:
    if x % 2 == 0:
        print(x + среднее)
    else:
        print(x)
