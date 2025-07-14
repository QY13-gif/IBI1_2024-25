seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
intron_count = 0 #Initiate the count of the intron
intron=[] #Initiate the intron
max_length=0 #Initiate the max length
largest_intron=[] #Initiate the largest intron
for i in range(len(seq)-1): #Traverse the sequence
    if seq[i]=="G" and seq[i+1]=="T": #Find the "GT"
        for j in range(i+2,len(seq)-1): #Traverse from the location of "GT" to the end of this sequence
            if seq[j]=="A" and seq[j+1]=="G": #Find the "AG"
                intron_count +=1 #Change the number og the count of the intron
                intron_seq=seq[i:j+2] #Identify the intron
                intron.append(intron_seq) #Add this intron
                current_length=len(intron_seq) #Calculate the length of this sequence
                if current_length > max_length:
                    max_length=current_length 
                    largest_intron=intron_seq #Identify the largest intron
#Print the count of introns, all the introns and the largest intron
print(f"The count of introns is {intron_count}")
print(f"All introns found: {intron}")
print(f"The largest intron is {largest_intron}")

