def count_substring(string, sub_string):
    count = 0
    n = len(sub_string)
    for i in range(len(string)):
        if string[i:i + n] == sub_string:
            count += 1
    return count
