def find_cut_sites(dna_seq, recognition_seq): #Make a function to identify if valid and to find the cut sites
    valid_nucleotides = {'A', 'C', 'G', 'T'} #Define the valid nucleotides
    if not all(nuc in valid_nucleotides for nuc in dna_seq): #Identify the DNA sequence valid
        return "Error: DNA sequence contains invalid nucleotides"
    
    if not all(nuc in valid_nucleotides for nuc in recognition_seq): #Identify the recogniton sequence valid
        return "Error: Recognition sequence contains invalid nucleotides"
    cut_sites=[] #Initiate the cut sites
    for i in range(len(dna_seq)-len(recognition_seq)+1): #Find the cut sites and add it 
        if dna_seq[i:i+len(recognition_seq)]== recognition_seq:
            cut_sites.append(i)
    return cut_sites
#Show an example
dna_seq="ATCGCCGTTACCGTA"
recognition_seq="CCG"
print(find_cut_sites(dna_seq, recognition_seq))


