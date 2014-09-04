#!/usr/bin/env python

import pandas as pd
import csv

f10_loc = "/Users/cmdb/data/results/SRR072905_clout/genes.fpkm_tracking"
f11_loc = "/Users/cmdb/data/results/SRR072906_clout/genes.fpkm_tracking"
f12_loc = "/Users/cmdb/data/results/SRR072907_clout/genes.fpkm_tracking"
f13_loc = "/Users/cmdb/data/results/SRR072908_clout/genes.fpkm_tracking"
f14A_loc = "/Users/cmdb/data/results/SRR072909_clout/genes.fpkm_tracking"
f14B_loc = "/Users/cmdb/data/results/SRR072911_clout/genes.fpkm_tracking"
f14C_loc = "/Users/cmdb/data/results/SRR072913_clout/genes.fpkm_tracking"
f14D_loc = "/Users/cmdb/data/results/SRR072915_clout/genes.fpkm_tracking"

# make list of all files
file_list = []
file_list.append(f10_loc)
file_list.append(f11_loc)
file_list.append(f12_loc)
file_list.append(f13_loc)
file_list.append(f14A_loc)
file_list.append(f14B_loc)
file_list.append(f14C_loc)
file_list.append(f14D_loc)

# cycle through files and pull out rows if they contain Sxl
sxl_list = []
for i in file_list:    
    with open(i) as file:
        for row in file:
            if "Sxl" in row:
                row = row.rstrip()
                sxl_list.append(row)

#make list with each entry in list being a list in which each entry is a column entry for that row
list_of_lists = []
for i in sxl_list:
    list_of_fields = []
    fields = i.rstrip("\r\n").split("\t")
    for field in fields:
        list_of_fields.append(field)
    list_of_lists.append(list_of_fields)

# write sxl data to csv file    
with open("female_sxl.csv", "wb") as f:
    writer = csv.writer(f, delimiter = "\t")
    writer.writerows(list_of_lists)
