rus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
lat = ["a","b","v","g","d","e","e","zh","z","i","y","k","l","m","n","o","p","r","s","t","u","f","h","ts","ch","sh","sch","","y","","e","yu","ya"]
rus_to_lat = {}
for i in range(len(rus)):
    rus_to_lat[rus[i]] = lat[i]

m = {
'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....','i':'..','j':'.---',
'k':'-.-','l':'.-..','m':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-',
'u':'..-','v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..',
'0':'-----','1':'.----','2':'..---','3':'...--','4':'....-',
'5':'.....','6':'-....','7':'--...','8':'---..','9':'----.'
}

s = input().strip().lower()
words = s.split()

for w in words:
    lat_w = ""
    for ch in w:
        if ch in rus_to_lat:
            lat_w += rus_to_lat[ch]
        elif ch in m:
            lat_w += ch
    out = []
    for ch in lat_w:
        if ch in m:
            out.append(m[ch])
    print(" ".join(out))
