слова = set()
while True:
    слово = input("ведите слово: ")
    if слово == "STOP":
        break
    слова.add(слово)
for s in sorted(слова):
    print(s)
