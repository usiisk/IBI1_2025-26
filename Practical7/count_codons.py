#!/usr/bin/env python
# count_codons.py
# Count the frequency of in-frame codons upstream of a given stop codon and plot a pie chart

import sys

# ==================== Environment check ====================
try:
    import matplotlib.pyplot as plt
    plt.switch_backend('Agg')
except ImportError as e:
    print("Error: matplotlib could not be imported. Please install it: pip install matplotlib")
    sys.exit(1)

# ==================== Fix font ====================
plt.rcParams['font.sans-serif'] = ['Arial']
plt.rcParams['axes.unicode_minus'] = False

# ==================== Parameter settings ====================
valid_stops = ['TAA', 'TAG', 'TGA']

while True:
    target_stop = input(f"Enter stop codon ({', '.join(valid_stops)}): ").upper().strip()
    if target_stop in valid_stops:
        break
    print(f"Invalid input. Choose from {valid_stops}.")

fasta_file = input("Enter FASTA file name (default: Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa): ").strip()
if not fasta_file:
    fasta_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"

# ==================== Read FASTA file ====================
genes = {}
current_id = None
current_seq_parts = []

try:
    with open(fasta_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith('>'):
                if current_id is not None:
                    genes[current_id] = ''.join(current_seq_parts)
                header = line[1:]
                current_id = header.split()[0]
                current_seq_parts = []
            else:
                current_seq_parts.append(line)
        if current_id is not None:
            genes[current_id] = ''.join(current_seq_parts)
except FileNotFoundError:
    print(f"Error: File '{fasta_file}' not found.")
    sys.exit(1)

print(f"Total genes read: {len(genes)}")

# ==================== Find ORFs (correct logic: use the last in-frame target stop codon) ====================
all_codon_counts = {}
genes_with_valid_orf = 0

for gene_name, seq in genes.items():
    seq = seq.upper()
    longest_orf_seq = ""
    max_orf_len = 0

    # Check all 3 reading frames
    for frame in range(3):
        i = frame
        while i + 3 <= len(seq):
            if seq[i:i+3] == 'ATG':
                start = i
                last_stop_pos = -1          # position of the last occurrence of target_stop in this frame
                pos = start + 3

                while pos + 3 <= len(seq):
                    codon = seq[pos:pos+3]
                    if codon in valid_stops:          # any stop codon ends translation
                        if codon == target_stop:      # record the position of this target stop
                            last_stop_pos = pos
                        break                         # stop scanning this reading frame (first stop encountered)
                    pos += 3

                if last_stop_pos != -1:
                    orf_len = last_stop_pos + 3 - start
                    if orf_len > max_orf_len:
                        max_orf_len = orf_len
                        longest_orf_seq = seq[start:last_stop_pos+3]
            i += 3

    if longest_orf_seq:
        genes_with_valid_orf += 1
        # Count all in-frame codons inside this ORF (excluding the stop codon)
        for k in range(0, len(longest_orf_seq) - 3, 3):
            codon = longest_orf_seq[k:k+3]
            if len(codon) == 3:
                all_codon_counts[codon] = all_codon_counts.get(codon, 0) + 1

if not all_codon_counts:
    print(f"No ORFs ending with {target_stop} found.")
    sys.exit(0)

print(f"\nGenes with ORF ending with {target_stop}: {genes_with_valid_orf}")
total_codons = sum(all_codon_counts.values())
print(f"Total codons counted: {total_codons}")

print("\nCodon counts upstream of stop codon:")
for codon, count in sorted(all_codon_counts.items()):
    print(f"{codon}: {count}")

# ==================== Plot ALL codons (no 'Other' grouping) ====================
sorted_items = sorted(all_codon_counts.items(), key=lambda x: x[1], reverse=True)

labels = [codon for codon, _ in sorted_items]
sizes = [count for _, count in sorted_items]

plt.figure(figsize=(14, 10))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 8})

plt.title(f"Codon Distribution Upstream of Stop Codon {target_stop}\nGenes: {genes_with_valid_orf}, Total Codons: {total_codons}")
plt.axis('equal')
plt.tight_layout()

output_file = f"codon_usage_{target_stop}.png"
plt.savefig(output_file, dpi=300, bbox_inches='tight')
print(f"\nPie chart saved as: {output_file}")
