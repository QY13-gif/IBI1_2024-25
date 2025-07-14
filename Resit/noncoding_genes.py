import re
def extract_gene_info(header_line):
    gene_name_match = re.search(r'gene:([^\s]+)', header_line)
    biotype_match = re.search(r'gene_biotype:([^\s]+)', header_line)
    gene_name = gene_name_match.group(1) if gene_name_match else ""
    is_noncoding = not (biotype_match and biotype_match.group(1) == "protein_coding")
    return gene_name, is_noncoding
def write_gene_entry(outfile, gene_name, sequence):
    if gene_name and sequence:
        outfile.write(f">{gene_name}\n{sequence}\n")
def process_fasta(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile: #Manage the input and output file
         current_gene = {
            'name': "",
            'sequence': "",
            'is_noncoding': False}
         for line in infile:
            if line.startswith('>'):
                if current_gene['is_noncoding']:
                    write_gene_entry(outfile, current_gene['name'], current_gene['sequence'])
                current_gene['name'], current_gene['is_noncoding'] = extract_gene_info(line)
                current_gene['sequence'] = ""
            else:
                current_gene['sequence'] += line.strip()
         if current_gene['is_noncoding']:
            write_gene_entry(outfile, current_gene['name'], current_gene['sequence'])

        
      
if __name__ == "__main__": 
    input_file=r'C:\Users\cqy111\Downloads\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa' #Iuput the file
    output_file="noncoding_genes.fa" #Identify the output file
    output_file= r'C:\Users\cqy111\Desktop\noncoding_gene.fa'
    process_fasta(input_file, output_file)