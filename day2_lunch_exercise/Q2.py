#!/usr/bin/env python

# finding number of alignments that are perfect matches to genome
sam_file = "/Users/cmdb/data/day1/tophat_out/accepted_hits.sam"

f = open(sam_file)

count = 0
for line in f:
    # NM:i:0 is Tag:type:value. Value is distance from reference (genome)
    if "NM:i:0" in line:
        count = count + 1
print count
    