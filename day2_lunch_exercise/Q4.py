#!/usr/bin/env python

# Extract only column containing chromosome for each read

sam_file = "/Users/cmdb/data/day1/tophat_out/accepted_hits.sam"

f = open(sam_file)

chromosome = []
for line in f:
    # split sam document on tabs (take out carriage returns and new lines)
    fields = line.rstrip("\r\n").split("\t")
    # column 3 in sam file contains chromosome data
    chromosome.append(fields[2])

print chromosome 