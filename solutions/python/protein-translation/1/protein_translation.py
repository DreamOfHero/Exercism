CODON_STOP = "STOP"
RNA = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine", "UUC": "Phenylalanine",
    "UUA": "Leucine", "UUG": "Leucine",
    "UCU": "Serine", "UCC": "Serine", "UCA": "Serine", "UCG": "Serine",
    "UAU": "Tyrosine", "UAC": "Tyrosine",
    "UGU": "Cysteine", "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": CODON_STOP, "UAG": CODON_STOP, "UGA": CODON_STOP
}

def proteins(strand):
    amino_acids = []
    # Iterate through the strand in chunks of 3
    for index_char in range(0, len(strand), 3):
        codon = strand[index_char: index_char + 3]
        
        # If a STOP codon is encountered, terminate translation immediately
        if RNA[codon] == CODON_STOP:
            break
            
        # Add the corresponding amino acid to the protein chain
        amino_acids.append(RNA[codon])
        
    return amino_acids