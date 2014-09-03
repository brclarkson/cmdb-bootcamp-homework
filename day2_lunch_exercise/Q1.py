#!/usr/bin/env python

sam_file = "/Users/cmdb/data/day1/tophat_out/accepted_hits.sam"

f = open(sam_file)

count = 0
for line in f:
    if "SRR" in line:
        count = count + 1
print count