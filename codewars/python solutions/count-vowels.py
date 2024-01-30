def get_count(sentence):
    vowels = "aeiou"
    result = 0

    for char in sentence:
        if char in vowels:
            result += 1
    return result
