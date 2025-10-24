rus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
lat = ["a","b","v","g","d","e","yo","zh","z","i","y","k","l","m","n","o","p","r","s","t","u","f","kh","ts","ch","sh","shch","\"","y","'","e","yu","ya"]

rus_to_lat = {}
for i in range(len(rus)):
    rus_to_lat[rus[i]] = lat[i]

text = input("введите текст:")
result = ""

for ch in text:
    low = ch.lower()
    if low in rus_to_lat:
        tr = rus_to_lat[low]
        if ch.isupper():
            if len(tr) > 1:
                tr = tr[0].upper() + tr[1:]
            else:
                tr = tr.upper()
        result += tr
    else:
        result += ch

print(result)
