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

'''
df_10 = pd.read_table( f10_loc )
df_11 = pd.read_table( f11_loc )
df_12 = pd.read_table( f12_loc )
df_13 = pd.read_table( f13_loc )
df_14A = pd.read_table( f14A_loc )
df_14B = pd.read_table( f14B_loc )
df_14C = pd.read_table( f14C_loc )
df_14D = pd.read_table( f14D_loc )
'''
file_list = []
file_list.append(f10_loc)
file_list.append(f11_loc)
file_list.append(f12_loc)
file_list.append(f13_loc)
file_list.append(f14A_loc)
file_list.append(f14B_loc)
file_list.append(f14C_loc)
file_list.append(f14D_loc)

sxl_list = []
for i in file_list:    
    with open(i) as file:
        for row in file:
            if "Sxl" in row:
                row = row.rstrip()
                sxl_list.append(row)

list_of_lists = []
for i in sxl_list:
    list_of_fields = []
    fields = i.rstrip("\r\n").split("\t")
    for field in fields:
        list_of_fields.append(field)
    list_of_lists.append(list_of_fields)

with open("female_sxl.csv", "wb") as f:
    writer = csv.writer(f, delimiter = "\t")
    writer.writerows(list_of_lists)
