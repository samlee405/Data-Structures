# TAA TAG TGA

def geneSearch(dna):
    returnList = []
    codon = []
    index = 0

    # ATGCA TGA ATGTAGATAGATGTGCCC
    while index <= len(dna) - 1:
        codon.append(dna[index])

        if dna[index] == "T" and index + 2 <= len(dna) - 1:
            if dna[index + 1] == "A":
                if dna[index + 2] == "A" or dna[index + 2] == "G":
                    # print(codon[:-1])
                    returnList.append("".join(codon[:-1]))
                    codon = []
                    index += 2

            elif dna[index + 1] == "G":
                if dna[index + 2] == "A":
                    # print(codon[:-1])
                    returnList.append("".join(codon[:-1]))
                    codon = []
                    index += 2

        index += 1

    returnList.append("".join(codon))

    return returnList


if __name__ == "__main__":
    print(geneSearch("ATG CAT GAA TGT AGA TAG ATG TGC CC"))

    # "ATGCA TGA ATG TAG A TAG ATGTGCCC"
    # "ATGCA ATG A ATGTGCCC"
