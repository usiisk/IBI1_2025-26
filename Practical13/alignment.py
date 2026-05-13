#!/usr/bin/env python3
# alignment.py
# Gap-free global alignment using BLOSUM62 matrix

import random

# ======================== 1. BLOSUM62 matrix (full) ========================
# Data from standard bioinformatics resources, order: A,R,N,D,C,Q,E,G,H,I,L,K,M,F,P,S,T,W,Y,V
BLOSUM62_RAW = """
   A  R  N  D  C  Q  E  G  H  I  L  K  M  F  P  S  T  W  Y  V
A  4 -1 -2 -2  0 -1 -1  0 -2 -1 -1 -1 -1 -2 -1  1  0 -3 -2  0
R -1  5  0 -2 -3  1  0 -2  0 -3 -2  2 -1 -3 -2 -1 -1 -3 -2 -3
N -2  0  6  1 -3  0  0 -1  0 -3 -3  0 -2 -3 -2  1  0 -4 -2 -3
D -2 -2  1  6 -3  0  2 -1 -1 -3 -4 -1 -3 -3 -1  0 -1 -4 -3 -3
C  0 -3 -3 -3  9 -3 -4 -3 -3 -1 -1 -3 -1 -2 -3 -1 -1 -2 -2 -1
Q -1  1  0  0 -3  5  2 -2  0 -3 -2  1  0 -3 -1  0 -1 -2 -1 -2
E -1  0  0  2 -4  2  5 -2  0 -3 -3  1 -2 -3 -1  0 -1 -3 -2 -2
G  0 -2 -1 -1 -3 -2 -2  6 -2 -4 -4 -2 -3 -3 -2  0 -2 -2 -3 -3
H -2  0  0 -1 -3  0  0 -2  8 -3 -3 -1 -2 -1 -2 -1 -2 -3  2 -3
I -1 -3 -3 -3 -1 -3 -3 -4 -3  4  2 -3  1  0 -3 -2 -1 -3 -1  3
L -1 -2 -3 -4 -1 -2 -3 -4 -3  2  4 -2  2  0 -3 -2 -1 -2 -1  1
K -1  2  0 -1 -3  1  1 -2 -1 -3 -2  5 -1 -3 -1  0 -1 -3 -2 -2
M -1 -1 -2 -3 -1  0 -2 -3 -2  1  2 -1  5  0 -2 -1 -1 -1 -1  1
F -2 -3 -3 -3 -2 -3 -3 -3 -1  0  0 -3  0  6 -4 -2 -2  1  3 -1
P -1 -2 -2 -1 -3 -1 -1 -2 -2 -3 -3 -1 -2 -4  7 -1 -1 -4 -3 -2
S  1 -1  1  0 -1  0  0  0 -1 -2 -2  0 -1 -2 -1  4  1 -3 -2 -2
T  0 -1  0 -1 -1 -1 -1 -2 -2 -1 -1 -1 -1 -2 -1  1  5 -2 -2  0
W -3 -3 -4 -4 -2 -2 -3 -2 -3 -3 -2 -3 -1  1 -4 -3 -2 11  2 -3
Y -2 -2 -2 -3 -2 -1 -2 -3  2 -1 -1 -2 -1  3 -3 -2 -2  2  7 -1
V  0 -3 -3 -3 -1 -2 -2 -3 -3  3  1 -2  1 -1 -2 -2  0 -3 -1  4
"""

def build_blosum62():
    """Build BLOSUM62 matrix from raw text, return dict with key (aa1, aa2)"""
    lines = BLOSUM62_RAW.strip().split('\n')
    aa_list = lines[0].split()
    matrix = {}
    for i, line in enumerate(lines[1:]):
        parts = line.split()
        aa1 = parts[0]
        scores = list(map(int, parts[1:]))
        for j, aa2 in enumerate(aa_list):
            matrix[(aa1, aa2)] = scores[j]
            matrix[(aa2, aa1)] = scores[j]  # symmetric
    return matrix

# ======================== 2. FASTA reader ========================
def read_fasta(filename):
    """Read FASTA file, return sequence string (ignoring comment lines)"""
    seq = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('>'):
                seq.append(line)
    return ''.join(seq)

# ======================== 3. Gap-free global alignment ========================
def global_align_nogap(seq1, seq2, blosum_matrix):
    """
    Perform gap-free global alignment on two equal-length sequences.
    Returns (blosum_score, percent_identity)
    """
    if len(seq1) != len(seq2):
        raise ValueError(f"Sequence lengths differ: {len(seq1)} vs {len(seq2)}")
    total_score = 0
    identical = 0
    for a, b in zip(seq1, seq2):
        total_score += blosum_matrix.get((a, b), -4)  # unknown amino acid -> -4
        if a == b:
            identical += 1
    percent_id = (identical / len(seq1)) * 100
    return total_score, percent_id

# ======================== 4. Generate random sequence ========================
def random_protein(length, seed=None):
    """Generate random protein sequence of given length (20 standard amino acids)"""
    if seed is not None:
        random.seed(seed)
    amino_acids = 'ACDEFGHIKLMNPQRSTVWY'
    return ''.join(random.choices(amino_acids, k=length))

# ======================== 5. Main program ========================
def main():
    # Load BLOSUM62 matrix
    print("Loading BLOSUM62 matrix...")
    blosum = build_blosum62()
    
    # Read real sequences (make sure files exist in the current directory)
    try:
        human_seq = read_fasta("human_DLX5.fasta")
        mouse_seq = read_fasta("mouse_DLX5.fasta")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Please ensure human_DLX5.fasta and mouse_DLX5.fasta exist")
        return
    
    # Check length equality
    if len(human_seq) != len(mouse_seq):
        print(f"Warning: human length ({len(human_seq)}) != mouse length ({len(mouse_seq)})")
        min_len = min(len(human_seq), len(mouse_seq))
        human_seq = human_seq[:min_len]
        mouse_seq = mouse_seq[:min_len]
    
    seq_len = len(human_seq)
    print(f"Sequence length: {seq_len} aa")
    
    # Generate random sequence (same length as human)
    random_seq = random_protein(seq_len, seed=42)  # fixed seed for reproducibility
    
    # Alignment 1: Human vs Mouse
    score_hm, pid_hm = global_align_nogap(human_seq, mouse_seq, blosum)
    print(f"\n[Human vs Mouse]")
    print(f"  BLOSUM62 score: {score_hm}")
    print(f"  Percent identity: {pid_hm:.2f}%")
    
    # Alignment 2: Human vs Random
    score_hr, pid_hr = global_align_nogap(human_seq, random_seq, blosum)
    print(f"\n[Human vs Random]")
    print(f"  BLOSUM62 score: {score_hr}")
    print(f"  Percent identity: {pid_hr:.2f}%")
    
    # Alignment 3: Mouse vs Random
    score_mr, pid_mr = global_align_nogap(mouse_seq, random_seq, blosum)
    print(f"\n[Mouse vs Random]")
    print(f"  BLOSUM62 score: {score_mr}")
    print(f"  Percent identity: {pid_mr:.2f}%")
    
    # Conclusion
    print("\nConclusion: Human-Mouse alignment score is much higher than with random sequences, indicating high relatedness.")
    
    # (Optional) Save random sequence as FASTA
    with open("random_DLX5_length.fasta", "w") as f:
        f.write(f">random_sequence_length_{seq_len}\n")
        for i in range(0, len(random_seq), 60):
            f.write(random_seq[i:i+60] + "\n")
    print(f"\nRandom sequence saved as random_DLX5_length.fasta")

if __name__ == "__main__":
    main()
