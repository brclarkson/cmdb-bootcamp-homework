#!/usr/bin/env python

import sys
from fasta import FASTAReader
import string
 

base_comp = { "A" : "T", "C" : "G", "G" : "C", "T" : "A"}

reader = FASTAReader( sys.stdin )

seq_list = []        
for sid, sequences in reader:
    seq_list.append(sequences)

# sort all items in sequence list by length (put in new list), sorted from longest to shortest
seq_sort = sorted(seq_list, key = len, reverse=True)

# take out hundred highest list entries and put in list
first_hundred = seq_sort[:100]

#make reverse complement of upper DNA strand    
rev_com_list = []
for i in first_hundred:
    rev_seq = "".join(i[::-1])
    rev_comp = [base_comp[b] for b in rev_seq]
    rev_comp_str = "".join(rev_comp)
    rev_com_list.append(rev_comp_str)
# WORKS UP TO HERE

#CODON DICTIONARY    
codontable = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }

#find ORFs and translate for upper strand 
# DOES NOT DO ANYTHING/WORK   
for seq in first_hundred:
    start = seq.find("ATG")
    stop = seq[start:].find("TAA") + start
    print start, stop
    
# does and ORF have a length req??
    
    
 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
