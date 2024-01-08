def DNA_strand(dna):
    result = ""

    for char in dna:
        if char == "A":
            result += "T"
        elif char == "T":
            result += "A"
        elif char == "C":
            result += "G"
        elif char == "G":
            result += "C"
    return result


# not the prettiest solution, but it works
