def get_hamming_distance(dna1, dna2):
    string1 = dna1.upper()
    string2 = dna2.upper()
    if len(string1) != len(string2):
        return('ERROR')
    hamming = 0
    for i in range (0, len(string1)):
        if string1[i] != string2[i]:
            hamming += 1
    return(hamming)

def get_dna_compliment(dna):
    compliment = dna.translate(dna.maketrans("ACGT", "TGCA")) [::-1]
    return compliment
