# protein_mass.py
# Practical 8 Part 1: Protein mass predictor

residue_masses = {
    'G': 57.02, 'A': 71.04, 'S': 87.03, 'P': 97.05, 'V': 99.07,
    'T': 101.05, 'C': 103.01, 'I': 113.08, 'L': 113.08, 'N': 114.04,
    'D': 115.03, 'Q': 128.06, 'K': 128.09, 'E': 129.04, 'M': 131.04,
    'H': 137.06, 'F': 147.07, 'R': 156.10, 'Y': 163.06, 'W': 186.08
}

def protein_mass(sequence):
    mass = 0.0
    for aa in sequence.upper():
        if aa not in residue_masses:
            raise ValueError(f"Unknown amino acid: '{aa}'")
        mass += residue_masses[aa]
    return mass

# Example call (required)
if __name__ == "__main__":
    example_seq = "ACDEFGHIKLMNPQRSTVWY"
    try:
        mass = protein_mass(example_seq)
        print(f"Example protein mass: {mass:.2f} amu")
    except ValueError as e:
        print(f"Error: {e}")
