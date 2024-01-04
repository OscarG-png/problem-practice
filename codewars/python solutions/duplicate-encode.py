def duplicate_encode(word):
    result = ""
    word = word.lower()
    for char in word:
        if word.count(char) > 1:
            result += ")"
        else:
            result += "("
    return result

# this one was a lot easier than I thought it would be
