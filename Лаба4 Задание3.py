numbers = []
for i in range(5):
    num = int(input(f"Введите число {i + 1}: "))
    numbers.append(num)
    for num in reversed(numbers):
        print(num, end=" ")
