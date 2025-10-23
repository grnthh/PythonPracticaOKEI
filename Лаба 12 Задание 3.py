f = open('C:/Users/d853/OneDrive/Рабочий стол/lines.txt','r', encoding='utf8')
lines = f.readlines()
f.close()

clean_lines = []
for line in lines:
    clean_line = line.strip()
    if clean_line:
        clean_lines.append(clean_line)

clean_lines.sort()

clean_lines.sort(key=len, reverse=True)

for line in clean_lines:
    print(line)