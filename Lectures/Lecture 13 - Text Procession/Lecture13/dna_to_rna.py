def main():
    dna = "ATGCCAATT"
    m_rna = dna_to_rna(dna)
    print(m_rna)

def dna_to_rna(dna):
    '''
    Each character in DNA corresponds to a character in mRNA
    T -> A
    A -> U
    C -> G
    G -> C
    >>> dna_to_rna("ATGCCAATT")
    'UACGGUUAA'
    '''
    dna = dna.replace('A', 'U')
    dna = dna.replace('T', 'A')
    # if I replace all Cs directly with Gs, the next line will
    # make them Cs again... so I use a temporary character X
    dna = dna.replace('C', 'X')
    dna = dna.replace('G', 'C')
    dna = dna.replace('X', 'G')
    return dna

if __name__ == '__main__':
    main()