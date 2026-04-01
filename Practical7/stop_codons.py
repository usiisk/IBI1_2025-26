input_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_file = 'stop_genes.fa'
with open(input_file, 'r') as fin, open(output_file, 'w') as fout:
    current_gene_name = ""
    current_sequence = ""
    for line in fin:
        line = line.strip()
        if line.startswith('>'):
          if current_sequence:
             found_stops = set()
             seq_len=len(current_sequence)
             for i in range(seq_len - 2):
                 if current_sequence[i:i+3]=='ATG':
                    for j in range(i+3, seq_len-2,3):
                        next_codon = current_sequence[j:j+3]
                        if next_codon in ('TAA','TAG','TGA'):
                            found_stops.add(next_codon)
                            break
             if found_stops:
                 stop_codon_str=' '.join(sorted(found_stops))
                 fout.write(f">{current_gene_name};{stop_codon_str}\n")
                 for k in range(0,len(current_sequence),80):
                     fout.write(current_sequence[k:k+80] + '\n')
          header=line[1:]
          current_gene_name=header.split()[0]
          current_sequence=""
        else:
            current_sequence+=line
    if current_sequence:
        found_stops=set()
        seq_len=len(current_sequence)
        for i in range(seq_len - 2):
            if current_sequence[i:i+3] == 'ATG':
                for j in range(i+3, seq_len-2, 3):
                    codon = current_sequence[j:j+3]
                    if codon in ('TAA', 'TAG', 'TGA'):
                        found_stops.add(codon)
                        break
        if found_stops:
            stop_codon_str = ' '.join(sorted(found_stops))
            fout.write(f">{current_gene_name};{stop_codon_str}\n")
            for k in range(0, len(current_sequence), 80):
                fout.write(current_sequence[k:k+80] + '\n') 
