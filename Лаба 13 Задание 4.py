db = {}

while True:
    line = input().strip()
    if line == "":
        break
    part = line.split()
    domain = part[0]
    ip = part[1]

    if ip not in db:
        db[ip] = []
    db[ip].append(domain)

ips = list(db.keys())
ips.sort()

for ip in ips:
    doms = db[ip]
    doms.sort()
    print(ip + ": " + ", ".join(doms) + " (" + str(len(doms)) + " шт.)")
