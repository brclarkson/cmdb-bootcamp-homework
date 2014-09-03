#!/usr/bin/env python

# finding number of reads mapped to exactly 1 location on genome

sam_file = "/Users/cmdb/data/day1/tophat_out/accepted_hits.sam"

f = open(sam_file)

count = 0
for line in f:
    if "NH:i:1" in line:
        count = count + 1
print count