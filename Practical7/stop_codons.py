# stop_codons.py
# Read yeast cDNA FASTA, filter genes containing stop codons, write simplified FASTA

import sys

stop_codons = ['TAA', 'TAG', 'TGA']
input_fasta = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"   
output_fasta = "stop_genes.fa"

def parse_fasta(filename):
    sequences = {}
    current_id = None
    current_seq = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith('>'):
                if current_id is not None:
                    sequences[current_id] = ''.join(current_seq)
                header = line[1:]
                gene_name = header.split()[0]
                current_id = gene_name
                current_seq = []
            else:
                current_seq.append(line)
        if current_id is not None:
            sequences[current_id] = ''.join(current_seq)
    return sequences

def check_stop_codons(seq):
    found = []
    for codon in stop_codons:
        if codon in seq.upper():
            found.append(codon)
    return found

try:
    sequences = parse_fasta(input_fasta)
except FileNotFoundError:
    print(f"Error: file {input_fasta} not found.")
    sys.exit(1)

with open(output_fasta, 'w') as out:
    for gene, seq in sequences.items():
        stops = check_stop_codons(seq)
        if stops:
            out.write(f">{gene} {','.join(stops)}\n")
            for i in range(0, len(seq), 60):
                out.write(seq[i:i+60] + '\n')
            out.write('\n')

print(f"Done. Filtered genes saved to {output_fasta}")
