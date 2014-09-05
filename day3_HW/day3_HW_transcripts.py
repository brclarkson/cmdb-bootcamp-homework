#!/usr/bin/env python

import sys
from fasta import FASTAReader
  
 """
 Take out the 100 longest sequences in a FASTA file
 """ 
        
reader = FASTAReader( sys.stdin )

seq_list = []        
for sid, sequences in reader:
    # take the first 30 characters of the gene ids so we know which genes we're looking at. Taking the first 30 characters means we know we'll have the gene name for each sequence contained in the label, and since each sequence has the same amount of added characters we don't have to worry about these seq ids in our length calculations
    seq_list.append(sid[:30] + ":" + sequences)

# sort all items in sequence list by length (put in new list), sorted from longest to shortest
seq_sort = sorted(seq_list, key = len, reverse=True)

# take out hundred highest list entries and put in list
first_hundred = seq_sort[:100]


