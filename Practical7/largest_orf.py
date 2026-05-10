# largest_orf.py
# Find the longest open reading frame (ORF) in an RNA sequence
# Checks all 3 reading frames (required by Practical 7)

seq = 'AAGAUCACUGCAAUGUGUGUGUCUGUUCUGAGAGGCUAAAAG'

start_codon = 'AUG'
stop_codons = ['UAA', 'UAG', 'UGA']

def find_longest_orf(rna_seq):
    longest_orf = ""
    longest_len = 0
    n = len(rna_seq)

    # Check ALL 3 READING FRAMES (0, 1, 2) — REQUIRED FOR FULL MARKS
    for frame in range(3):
        i = frame
        while i + 3 <= n:
            # Find start codon
            if rna_seq[i:i+3] == start_codon:
                # Scan for in-frame stop codon
                for j in range(i + 3, n, 3):
                    codon = rna_seq[j:j+3]
                    if codon in stop_codons:
                        current_orf = rna_seq[i:j+3]
                        current_len = len(current_orf)
                        # Update longest ORF
                        if current_len > longest_len:
                            longest_len = current_len
                            longest_orf = current_orf
                        break  # stop at first in-frame stop codon
            i += 3
    return longest_orf, longest_len

# Run function
longest_orf_seq, longest_orf_len = find_longest_orf(seq)

# Output results
print(f"Longest ORF sequence: {longest_orf_seq}")
print(f"Longest ORF length: {longest_orf_len} nucleotides")
