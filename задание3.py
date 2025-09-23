h = int(input("введите текущий час: "))
m = int(input("введите текущую минуту: "))
t = int(input("введите время доставки: "))
if not (0 <= h < 24 and 0 <= m < 60 and 30 <= t <= 10 ** 9):
    print("некорректное время")
total = h * 60 + m + t
h, m = divmod(total % (24 * 60), 60)
print(f"{h:02d}:{m:02d}")
