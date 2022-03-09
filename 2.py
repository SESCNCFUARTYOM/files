if __name__ == "__main__":
    with open("file.txt", "r", encoding="utf-8") as f:
        a = f.read().split()

    longest = a[0]
    for i in a:
        if len(i) > len(longest):
            longest = i

    count = 0
    for i in a:
        if i == longest:
            count += 1

    print(longest, count)
