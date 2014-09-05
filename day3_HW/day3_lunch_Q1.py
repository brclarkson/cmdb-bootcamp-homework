#!/usr/bin/env python

"""
Parse a blast output file and give some information about it
***DOES NOT WORK***
"""

import sys
from BLASTReader import BLASTReader
        
reader = BLASTReader( sys.stdin )        

for last_fid, last_hid, sequence in reader:
    print last_fid, last_hid, sequence