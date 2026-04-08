# Monoisotopic residue masses (amu)
RESIDUE_MASS = {
    'G': 57.02,   # Glycine
    'A': 71.04,   # Alanine
    'S': 87.03,   # Serine
    'P': 97.05,   # Proline
    'V': 99.07,   # Valine
    'T': 101.05,  # Threonine
    'C': 103.01,  # Cysteine
    'I': 113.08,  # Isoleucine
    'L': 113.08,  # Leucine
    'N': 114.04,  # Asparagine
    'D': 115.03,  # Aspartic Acid
    'Q': 128.06,  # Glutamine
    'K': 128.09,  # Lysine
    'E': 129.04,  # Glutamic Acid
    'M': 131.04,  # Methionine
    'H': 137.06,  # Histidine
    'F': 147.07,  # Phenylalanine
    'R': 156.10,  # Arginine
    'Y': 163.06,  # Tyrosine
    'W': 186.08   # Tryptophan
}

def protein_mass(sequence):
    """
    Calculate the total mass of a protein from its amino acid sequence.

    Args:
        sequence (str): String of single-letter amino acid codes (uppercase).

    Returns:
        float: Total mass in atomic mass units (amu).

    Raises:
        ValueError: If any amino acid is not found in the mass table.
    """
    total = 0.0
    for aa in sequence:
        if aa not in RESIDUE_MASS:
            raise ValueError(f"Unknown amino acid: '{aa}'. Valid letters: {''.join(RESIDUE_MASS.keys())}")
        total += RESIDUE_MASS[aa]
    return total

# Example function call
if __name__ == "__main__":
    # Example 1: Valid sequence
    seq1 = "AG"   # Alanine + Glycine
    mass1 = protein_mass(seq1)
    print(f"Protein mass of '{seq1}': {mass1} amu")

    # Example 2: Longer valid sequence (e.g., a small peptide)
    seq2 = "MVLSPADKTNVKAAW"  # part of hemoglobin
    mass2 = protein_mass(seq2)
    print(f"Protein mass of '{seq2}': {mass2:.2f} amu")

    # Example 3: Invalid sequence (will raise an error)
    try:
        seq3 = "HELLO"   # 'O' is not a valid amino acid
        mass3 = protein_mass(seq3)
        print(f"Protein mass of '{seq3}': {mass3} amu")
    except ValueError as e:
        print(f"Error: {e}")
