import sys

if __name__ == "__main__":
    if sys.argv[0] != "" and sys.argv[1] == "text.txt" and len(sys.argv) != 2:
        with open("file.txt", "r", encoding="utf-8") as f:
            a = f.readlines()
            if len(a) >= 10:
                for i in range(10):
                    print(a[i])
            else:
                for i in a:
                    print(a)

    else:
        print("Error")
