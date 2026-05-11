# largest_orf.py
# Find the longest open reading frame (ORF) in an RNA sequence
# Uses the correct sequence from Practical 7 guide

seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'

start_codon = 'AUG'
stop_codons = ['UAA', 'UAG', 'UGA']

def find_longest_orf(rna_seq):
    longest_orf = ""
    longest_len = 0
    n = len(rna_seq)

    # Check all 3 reading frames
    for frame in range(3):
        i = frame
        while i + 3 <= n:
            if rna_seq[i:i+3] == start_codon:
                # Scan downstream in steps of 3
                for j in range(i + 3, n, 3):
                    codon = rna_seq[j:j+3]
                    if codon in stop_codons:
                        current_orf = rna_seq[i:j+3]
                        current_len = len(current_orf)
                        if current_len > longest_len:
                            longest_len = current_len
                            longest_orf = current_orf
                        break  # stop at first in-frame stop codon
            i += 3
    return longest_orf, longest_len

longest_orf_seq, longest_orf_len = find_longest_orf(seq)
print(f"Longest ORF sequence: {longest_orf_seq}")
print(f"Longest ORF length: {longest_orf_len} nucleotides")
