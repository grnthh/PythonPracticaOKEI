count = int(input("Сколько чисел Фибоначчи вывести? "))
a = 0
b = 1
n = 0
while n < count:
    print(a)
    c = a + b
    a = b
    b = c
    n = n + 1
