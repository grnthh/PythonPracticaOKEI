matrix = []
print("введите 100 чисел для матрицы 10x10:")
for i in range(10):
    row = []
    for j in range(10):
        num = int(input(f"Элемент [{i+1},{j+1}]: "))
        row.append(num)
    matrix.append(row)
row_sums = [sum(row) for row in matrix]
col_products = [1] * 10
for i in range(10):
    for j in range(10):
        col_products[j] *= matrix[i][j]
print("\nматрица:")
for row in matrix:
    print(row)
print("\nсуммы строк:", row_sums)
print("произведения столбцов:", col_products)
print("\nмаксимальная сумма строки:", max(row_sums))
print("максимальное произведение столбца:", max(col_products))