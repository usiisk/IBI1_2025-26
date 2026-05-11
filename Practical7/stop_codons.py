# Set input and output file names
input_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_file = 'stop_genes.fa'

# Open input file for reading and output file for writing
with open(input_file, 'r') as fin, open(output_file, 'w') as fout:
    # Initialize variables to store current gene information
    current_gene_name = ""
    current_sequence = ""

    # Read each line of the input file
    for line in fin:
        line = line.strip()  # Remove whitespace and newlines

        # Check if the line is a FASTA header (starts with '>')
        if line.startswith('>'):
            # If there is a stored gene sequence, process it
            if current_sequence:
                # Create a set to store found stop codons
                found_stops = set()
                seq_len = len(current_sequence)

                # Search for START codon (ATG) in the sequence
                for i in range(seq_len - 2):
                    if current_sequence[i:i+3] == 'ATG':
                        # Once ATG found, search for STOP codon in frame
                        for j in range(i+3, seq_len-2, 3):
                            next_codon = current_sequence[j:j+3]
                            # Check if codon is a stop codon (TAA, TAG, TGA)
                            if next_codon in ('TAA','TAG','TGA'):
                                found_stops.add(next_codon)
                                break  # Stop after finding the first stop codon

                # If stop codon was found, write the gene to output
                if found_stops:
                    # Format stop codon string
                    stop_codon_str = ' '.join(sorted(found_stops))
                    # Write new FASTA header with gene name and stop codon
                    fout.write(f">{current_gene_name};{stop_codon_str}\n")
                    # Write sequence with 80 characters per line
                    for k in range(0, len(current_sequence), 80):
                        fout.write(current_sequence[k:k+80] + '\n')

            # Process new header: extract gene name
            header = line[1:]
            current_gene_name = header.split()[0]
            # Reset sequence for the new gene
            current_sequence = ""

        # If line is not a header, it's part of the sequence
        else:
            # Append line to the current gene sequence
            current_sequence += line

    # After loop ends, process the LAST gene in the file
    if current_sequence:
        found_stops = set()
        seq_len = len(current_sequence)
        # Same logic: find ATG then stop codon
        for i in range(seq_len - 2):
            if current_sequence[i:i+3] == 'ATG':
                for j in range(i+3, seq_len-2, 3):
                    codon = current_sequence[j:j+3]
                    if codon in ('TAA', 'TAG', 'TGA'):
                        found_stops.add(codon)
                        break
        # Write last gene if valid
        if found_stops:
            stop_codon_str = ' '.join(sorted(found_stops))
            fout.write(f">{current_gene_name};{stop_codon_str}\n")
            for k in range(0, len(current_sequence), 80):
                fout.write(current_sequence[k:k+80] + '\n')
