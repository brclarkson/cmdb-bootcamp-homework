#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

# I have no headers in my csv file, so I need to specify that so pandas doesn't call the first row a header
sxl_df = pd.read_table("/Users/cmdb/cmdb-bootcamp-homework/day2_HW/female_sxl.csv", header = None)


plt.figure()
# FPKM data is contained in column 9 (starting at 0), so I specify that I want the 9th value in each row for the y data
sxl_df.plot( y=9 )
plt.savefig("female_sxl_plot.png")