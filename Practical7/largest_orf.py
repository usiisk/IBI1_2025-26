# largest_orf.py
# Find the longest open reading frame (ORF) in an RNA sequence

seq = 'AAGAUCACUGCAAUGUGUGUGUCUGUUCUGAGAGGCUAAAAG'

start_codon = 'AUG'
stop_codons = ['UAA', 'UAG', 'UGA']

def find_longest_orf(rna_seq):
    longest_orf = ""
    longest_len = 0
    n = len(rna_seq)
    for i in range(n):
        if rna_seq[i:i+3] == start_codon:
            for j in range(i+3, n, 3):
                codon = rna_seq[j:j+3]
                if codon in stop_codons:
                    orf_seq = rna_seq[i:j+3]
                    orf_len = len(orf_seq)
                    if orf_len > longest_len:
                        longest_len = orf_len
                        longest_orf = orf_seq
                    break
    return longest_orf, longest_len

longest_orf_seq, longest_orf_len = find_longest_orf(seq)
print(f"Longest ORF sequence: {longest_orf_seq}")
print(f"Longest ORF length: {longest_orf_len} nucleotides")
