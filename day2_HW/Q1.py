#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

#make data frame for male data
cufflinks_output1 = "/Users/cmdb/data/results/SRR072893_clout/genes.fpkm_tracking"
df1 = pd.read_table( cufflinks_output1 )

#make data frame for female data
cufflinks_output2 = "/Users/cmdb/data/results/SRR072915_clout/genes.fpkm_tracking"
df2 = pd.read_table(cufflinks_output2)

# 15602 rows in data frame, 1/3 is 5200.66. I will use 5201, 5201, 5200 for the thirds
# Divide the data sets into thirds 
# first = bottom, second = middle, third = top for later
df1_firstthird = df1.sort("FPKM")[:5201]
df1_secondthird = df1.sort("FPKM")[5201:10402]
df1_thirdthird = df1.sort("FPKM")[10402:]

df2_firstthird = df2.sort("FPKM")[:5201]
df2_secondthird = df2.sort("FPKM")[5201:10402]
df2_thirdthird = df2.sort("FPKM")[10402:]

# make list of all the necessary data sets
master_list = []
for i in df1_firstthird["FPKM"], df1_secondthird["FPKM"], df1_thirdthird["FPKM"], df2_firstthird["FPKM"], df2_secondthird["FPKM"], df2_thirdthird["FPKM"]:
    master_list.append(i)
    
# make canvas
plt.figure()

plt.axis([0, 100, 0, 100])

plt.boxplot(master_list)
plt.savefig("Q1_boxplots.png")

