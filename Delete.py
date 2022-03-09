path = input()
with open(path, "r", encoding="utf-8") as f:
    a = f.readlines()

with open("file.py", "w", encoding="utf-8") as f:
    for i in a:
        for j in i:
            if j == "#":
                i = i[:i.find(j)]
        f.write(i)


