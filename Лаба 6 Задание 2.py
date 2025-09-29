x = int(input("введите количество ячеек: "))
arr = [0] * x
left = 0
right = x - 1
i = 0
while left <= right:
    val = input(f"введите значение №{i+1}: ")
    arr[right] = val
    i += 1
    if left <= right and i < x:
        val = input(f"введите значение №{i+1}: ")
        arr[left] = val
        i += 1
    left += 1
    right -= 1
print("результат:", arr)