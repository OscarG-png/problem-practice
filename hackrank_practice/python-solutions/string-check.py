def alnumCheck(s):
    for char in s:
        if char.isalnum():
            return True
    return False


def alphaCheck(s):
    for char in s:
        if char.isalpha():
            return True
    return False


def digitCheck(s):
    for char in s:
        if char.isdigit():
            return True
    return False


def lowerCheck(s):
    for char in s:
        if char.islower():
            return True
    return False


def upperCheck(s):
    for char in s:
        if char.isupper():
            return True
    return False


if __name__ == '__main__':
    s = input()
    print(alnumCheck(s))
    print(alphaCheck(s))
    print(digitCheck(s))
    print(lowerCheck(s))
    print(upperCheck(s))
