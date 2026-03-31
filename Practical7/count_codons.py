# count_codons.py
# Count upstream in-frame codons for a given stop codon and plot pie chart

import matplotlib.pyplot as plt
import sys

print("Enter a stop codon (TAA, TAG, TGA):")
user_stop = input().strip().upper()
if user_stop not in ['TAA', 'TAG', 'TGA']:
    print("Error: please enter TAA, TAG, or TGA")
    sys.exit(1)

input_fasta = "stop_genes.fa"

def parse_fasta_simple(filename):
    genes = []
    with open(filename, 'r') as f:
        current_header = None
        current_seq = []
        for line in f:
            line = line.strip()
            if not line:
                if current_header is not None:
                    genes.append((current_header, ''.join(current_seq)))
                    current_header = None
                    current_seq = []
                continue
            if line.startswith('>'):
                if current_header is not None:
                    genes.append((current_header, ''.join(current_seq)))
                current_header = line[1:]
                current_seq = []
            else:
                current_seq.append(line)
        if current_header is not None:
            genes.append((current_header, ''.join(current_seq)))
    return genes

def get_upstream_codons(seq, stop_codon):
    seq = seq.upper()
    best_codons = []
    max_upstream = -1
    for frame in range(3):
        i = frame
        while i + 3 <= len(seq):
            codon = seq[i:i+3]
            if codon == stop_codon:
                upstream = []
                pos = frame
                while pos < i:
                    upstream.append(seq[pos:pos+3])
                    pos += 3
                if len(upstream) > max_upstream:
                    max_upstream = len(upstream)
                    best_codons = upstream
            i += 3
    return best_codons

genes = parse_fasta_simple(input_fasta)
filtered_genes = []
for header, seq in genes:
    parts = header.split()
    if len(parts) >= 2:
        stops_in_header = parts[1].split(',')
        if user_stop in stops_in_header:
            filtered_genes.append((header, seq))

if not filtered_genes:
    print(f"No genes found containing {user_stop}.")
    sys.exit(0)

codon_counts = {}
for header, seq in filtered_genes:
    upstream = get_upstream_codons(seq, user_stop)
    for codon in upstream:
        if len(codon) == 3:
            codon_counts[codon] = codon_counts.get(codon, 0) + 1

if not codon_counts:
    print("No upstream codons found.")
    sys.exit(0)

sorted_items = sorted(codon_counts.items(), key=lambda x: x[1], reverse=True)
top10 = sorted_items[:10]
others_count = sum(count for _, count in sorted_items[10:])

labels = [codon for codon, _ in top10]
sizes = [count for _, count in top10]
if others_count > 0:
    labels.append('Other')
    sizes.append(others_count)

plt.figure(figsize=(10, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title(f'Distribution of upstream in-frame codons for stop codon {user_stop}')
plt.axis('equal')
output_png = f'codon_usage_{user_stop}.png'
plt.savefig(output_png, dpi=300, bbox_inches='tight')
print(f"Pie chart saved as {output_png}")# count_codons.py
# Count upstream in-frame codons for a given stop codon and plot pie chart

import matplotlib.pyplot as plt
import sys

print("Enter a stop codon (TAA, TAG, TGA):")
user_stop = input().strip().upper()
if user_stop not in ['TAA', 'TAG', 'TGA']:
    print("Error: please enter TAA, TAG, or TGA")
    sys.exit(1)

input_fasta = "stop_genes.fa"

def parse_fasta_simple(filename):
    genes = []
    with open(filename, 'r') as f:
        current_header = None
        current_seq = []
        for line in f:
            line = line.strip()
            if not line:
                if current_header is not None:
                    genes.append((current_header, ''.join(current_seq)))
                    current_header = None
                    current_seq = []
                continue
            if line.startswith('>'):
                if current_header is not None:
                    genes.append((current_header, ''.join(current_seq)))
                current_header = line[1:]
                current_seq = []
            else:
                current_seq.append(line)
        if current_header is not None:
            genes.append((current_header, ''.join(current_seq)))
    return genes

def get_upstream_codons(seq, stop_codon):
    seq = seq.upper()
    best_codons = []
    max_upstream = -1
    for frame in range(3):
        i = frame
        while i + 3 <= len(seq):
            codon = seq[i:i+3]
            if codon == stop_codon:
                upstream = []
                pos = frame
                while pos < i:
                    upstream.append(seq[pos:pos+3])
                    pos += 3
                if len(upstream) > max_upstream:
                    max_upstream = len(upstream)
                    best_codons = upstream
            i += 3
    return best_codons

genes = parse_fasta_simple(input_fasta)
filtered_genes = []
for header, seq in genes:
    parts = header.split()
    if len(parts) >= 2:
        stops_in_header = parts[1].split(',')
        if user_stop in stops_in_header:
            filtered_genes.append((header, seq))

if not filtered_genes:
    print(f"No genes found containing {user_stop}.")
    sys.exit(0)

codon_counts = {}
for header, seq in filtered_genes:
    upstream = get_upstream_codons(seq, user_stop)
    for codon in upstream:
        if len(codon) == 3:
            codon_counts[codon] = codon_counts.get(codon, 0) + 1

if not codon_counts:
    print("No upstream codons found.")
    sys.exit(0)

sorted_items = sorted(codon_counts.items(), key=lambda x: x[1], reverse=True)
top10 = sorted_items[:10]
others_count = sum(count for _, count in sorted_items[10:])

labels = [codon for codon, _ in top10]
sizes = [count for _, count in top10]
if others_count > 0:
    labels.append('Other')
    sizes.append(others_count)

plt.figure(figsize=(10, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title(f'Distribution of upstream in-frame codons for stop codon {user_stop}')
plt.axis('equal')
output_png = f'codon_usage_{user_stop}.png'
plt.savefig(output_png, dpi=300, bbox_inches='tight')
print(f"Pie chart saved as {output_png}")
