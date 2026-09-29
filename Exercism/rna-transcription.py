"""Module, that contains function translating DNA to RNA."""
def to_rna(dna_strand):
    """Function translating DNA to RNA."""
    dna = list(dna_strand)
    transcribtions = {"G": "C", "C": "G", "T": "A", "A":"U"}
    rna = [transcribtions[nucl] for nucl in dna]
    return "".join(rna)
