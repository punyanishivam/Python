def DNA_strand(dna):
    result = ""
    for i in range(len(dna)):
        if dna[i] == "A":
            result += "T"
        elif dna[i] == "T":
            result += "A"
        elif dna[i] == "G":
            result += "C"
        elif dna[i] == "C":
            result += "G"
        else:
            result += dna[i]

    return result


dna = "AAAA"
print(DNA_strand(dna))
