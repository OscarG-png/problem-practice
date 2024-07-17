def main():
    codes = open("codes.txt").read().splitlines()
    answer = 0

    def findFirst(data: str):
        for c in data:
            if c.isnumeric():
                return c

    def findLast(data: str):
        for i in range(len(data)-1, -1, -1):
            if data[i].isnumeric():
                return data[i]

    for code in codes:
        first = findFirst(code)
        last = findLast(code)
        concatNumber = first + last
        answer += int(concatNumber)

    print(answer)


if __name__ == "__main__":
    main()
