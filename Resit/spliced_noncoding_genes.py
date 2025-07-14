import re

def extract_gene_info(header_line):
    gene_match = re.search(r'gene:([^\s]+)', header_line)
    biotype_match = re.search(r'gene_biotype:([^\s]+)', header_line)
    
    gene_name = gene_match.group(1) if gene_match else ""
    is_noncoding = not (biotype_match and biotype_match.group(1) == "protein_coding")
    
    return gene_name, is_noncoding

def count_introns(sequence, donor, acceptor):
    pattern = re.compile(f"{re.escape(donor)}.*?{re.escape(acceptor)}")
    return len(pattern.findall(sequence))

def process_spliced_genes(input_file, output_file, donor, acceptor):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        current_gene = {
            'name': "",
            'sequence': "",
            'is_noncoding': False
        }
        
        for line in infile:
            if line.startswith('>'):
                if current_gene['is_noncoding'] and current_gene['sequence']:
                    intron_count = count_introns(current_gene['sequence'], donor, acceptor)
                    if intron_count > 0:
                        outfile.write(f">{current_gene['name']} introns:{intron_count}\n")
                        outfile.write(f"{current_gene['sequence']}\n")
                
                current_gene['name'], current_gene['is_noncoding'] = extract_gene_info(line)
                current_gene['sequence'] = ""
            else:
                current_gene['sequence'] += line.strip()
        
        if current_gene['is_noncoding'] and current_gene['sequence']:
            intron_count = count_introns(current_gene['sequence'], donor, acceptor)
            if intron_count > 0:
                outfile.write(f">{current_gene['name']} introns:{intron_count}\n")
                outfile.write(f"{current_gene['sequence']}\n")

if __name__ == "__main__":
    input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
    valid_combinations = ['GTAG', 'GCAG', 'ATAC']
    
    user_input = input(f"Please enter the combination of splicing sites ({', '.join(valid_combinations)}): ").upper()
    while user_input not in valid_combinations:
        print(f"Invalid input. Please select: {valid_combinations}")
        user_input = input("Please inter again: ").upper()
    
    donor, acceptor = user_input[:2], user_input[2:]
    output_file = f"{user_input}_spliced_genes.fa"
    input_file=r'C:\Users\cqy111\Downloads\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
    from pathlib import Path  
    output_file = str(Path.home() / "Desktop" / f"{user_input}_spliced_genes.fa")  
    
    

    process_spliced_genes(input_file, output_file, donor, acceptor)
    print(f"Results has been saved into {output_file}")