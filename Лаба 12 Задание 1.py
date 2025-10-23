numbers = input("введите числа через пробел: ").split()
numbers = [int(num) for num in numbers]
сумма_квадратов = sum(num ** 2 for num in numbers if num % 2 != 0)
print("сумма квадратов нечетных чисел", сумма_квадратов)
