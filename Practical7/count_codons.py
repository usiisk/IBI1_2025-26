#!/usr/bin/env python
# count_codons.py
# Count the frequency of in-frame codons upstream of a given stop codon and plot a pie chart

import sys

# ==================== Environment check ====================
try:
    import matplotlib.pyplot as plt
    plt.switch_backend('Agg')          # Use non-interactive backend to avoid GUI dependency
except ImportError as e:
    print("Error: matplotlib could not be imported. Please install it with:")
    print("  pip install matplotlib")
    print("If already installed, check your Python environment.")
    sys.exit(1)
except Exception as e:
    print(f"Error importing matplotlib: {e}")
    print("Please try running this script with the Miniconda Python environment.")
    sys.exit(1)

# ==================== Parameter settings ====================
valid_stops = ['TAA', 'TAG', 'TGA']

# Get user input for stop codon
while True:
    target_stop = input(f"Enter stop codon ({', '.join(valid_stops)}): ").upper().strip()
    if target_stop in valid_stops:
        break
    print(f"Invalid input. Please choose from {valid_stops}.")

# Input file (you can change to your actual file name)
fasta_file = input("Enter FASTA file name (default: Saccharomyces_cerevisiae.cdna.all.fa): ").strip()
if not fasta_file:
    fasta_file = "Saccharomyces_cerevisiae.cdna.all.fa"

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
                # Extract gene name: take the first word after '>'
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

# ==================== Find the longest ORF and count codons ====================
all_codon_counts = {}
genes_with_valid_orf = 0

for gene_name, seq in genes.items():
    seq = seq.upper()          # Convert to uppercase
    longest_orf_seq = ""       # Longest ORF sequence for this gene
    max_orf_len = 0

    # Try three reading frames
    for frame in range(3):
        i = frame
        while i + 3 <= len(seq):
            if seq[i:i+3] == 'ATG':                # Start codon found
                start = i
                # Scan the reading frame for all occurrences of target_stop
                last_stop_pos = -1
                pos = start + 3
                while pos + 3 <= len(seq):
                    codon = seq[pos:pos+3]
                    if codon == target_stop:
                        last_stop_pos = pos       # Record the last occurrence
                    elif codon in valid_stops:     # Other stop codon ends this reading frame
                        break
                    pos += 3
                if last_stop_pos != -1:
                    orf_len = last_stop_pos + 3 - start
                    if orf_len > max_orf_len:
                        max_orf_len = orf_len
                        longest_orf_seq = seq[start:last_stop_pos+3]
            i += 3

    if longest_orf_seq:
        genes_with_valid_orf += 1
        # Count all codons inside this ORF (excluding the stop codon)
        # Start from the start codon and go up to the stop codon (step 3)
        for k in range(0, len(longest_orf_seq) - 3, 3):
            codon = longest_orf_seq[k:k+3]
            if len(codon) == 3:
                all_codon_counts[codon] = all_codon_counts.get(codon, 0) + 1

if not all_codon_counts:
    print(f"No ORFs ending with {target_stop} were found.")
    sys.exit(0)

print(f"\nAmong {len(genes)} genes, {genes_with_valid_orf} contain an ORF ending with {target_stop}.")
total_codons = sum(all_codon_counts.values())
print(f"Total codons counted: {total_codons}")

# ==================== Plot pie chart ====================
# Sort by count descending
sorted_items = sorted(all_codon_counts.items(), key=lambda x: x[1], reverse=True)

# Show only top 10, merge the rest into 'Other'
top_n = 10
top_items = sorted_items[:top_n]
others_count = sum(count for _, count in sorted_items[top_n:])

labels = [codon for codon, _ in top_items]
sizes = [count for _, count in top_items]
if others_count > 0:
    labels.append('Other')
    sizes.append(others_count)

plt.figure(figsize=(12, 8))
wedges, texts, autotexts = plt.pie(sizes, labels=labels, autopct='%1.1f%%',
                                   startangle=140, textprops={'fontsize': 10})
plt.title(f"Distribution of in-frame codons upstream of stop codon {target_stop}\n"
          f"(Based on {genes_with_valid_orf} genes, {total_codons} codons)")

# Beautify percentage text
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

plt.axis('equal')
plt.tight_layout()

output_file = f"codon_usage_{target_stop}.png"
plt.savefig(output_file, dpi=300)
print(f"\nPie chart saved as: {output_file}")

# Optional: display the chart (uncomment if GUI is available)
# plt.show()
