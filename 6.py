import sys
import os

if __name__ == "__main__":
    file = []
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            f = sys.argv[i]
            if os.path.isfile(f):
                file.append(f)
                continue
            print(f"File {f} doesn't exist")
    else:
        print("Not enough arguments!")
        sys.exit()
    fun = []
    for i in file:
        with open(i, "r", encoding="utf-8") as f:
            a = f.readlines()
        for j in range(len(a)):
            if a[j].startswith("def "):
                if not a[j - 1].startswith("#"):
                    fun.append(f"file name: {i}, line: {j} function name: {a[j][4:]}")

    for i in fun:
        print(i)