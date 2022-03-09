if __name__ == "__main__":
    with open("file.txt", "r", encoding="utf-8") as f:
        a = f.readlines()
    for i in a:
        if "," in i:
            print(i)
            