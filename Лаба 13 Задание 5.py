data = {}

while True:
    try:
        line = input("введите покупателя, товар, количество купленного товара покупателем: ").strip()
        if not line:
            break
        buyer, product, amount = line.split()
        amount = int(amount)

        if buyer not in data:
            data[buyer] = {}
        if product not in data[buyer]:
            data[buyer][product] = 0
        data[buyer][product] += amount
    except EOFError:
        break
for buyer in sorted(data.keys()):
    print(f"{buyer}:")
    for product in sorted(data[buyer].keys()):
        print(product, data[buyer][product])
