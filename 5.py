import string

if __name__ == "__main__":
    path = input("Enter a path to file: ")
    with open(path, "r", encoding="utf-8") as f:
        a = f.read().lower().split()

    print(a)

    lowest_percentage_key = ""
    lowest_percentage = 100
    for i in list(string.ascii_lowercase):
        count = 0
        for j in a:
            if i in j:
                count += 1

        percentage = round(count / len(a) * 100, 2)
        if percentage < lowest_percentage:
            lowest_percentage_key = i
            lowest_percentage = percentage
        print(f"{i}: {percentage}%")

    print(f"{lowest_percentage_key} is the rarest with the percentage of {lowest_percentage}%")
