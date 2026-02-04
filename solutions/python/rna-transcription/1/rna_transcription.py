def to_rna(dna_strand):
    """Return the RNA complement of a DNA strand."""
    # Mapping from DNA nucleotides to RNA nucleotides
    DNA_TO_RNA = {
        "C": "G",
        "G": "C",
        "T": "A",
        "A": "U",
    }

    rna_strand = []

    # Transcribe each DNA nucleotide to its RNA complement
    for dna_char in dna_strand:
        rna_strand.append(DNA_TO_RNA[dna_char])

    # Combine all RNA nucleotides into a single string
    return "".join(rna_strand)
