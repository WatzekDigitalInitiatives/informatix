# -*- coding: utf-8 -*-
"""
Created on Fri May 20 09:21:00 2016

@author: rishijavia
"""

import sys

if len(sys.argv) != 3:
    sys.exit("Please run the file as python find_unavailable_seqid.py database.fasta names.txt")
    
if sys.argv[-2].endswith('.fasta') and sys.argv[-2].endswith('.txt'):
    input_db = sys.argv[-2]
    with open(input_db, 'r') as f:
        data = f.read().splitlines()
             
    input_names = sys.argv[-1]
    with open(input_names, 'r') as f:
        names = f.read().splitlines()
    
    data_list = []
    names_list = names
    for i in range(0, len(data), 2):
        data_list.append(data[i][1:])
     
    counter = 0
    for val in names_list:
        if val in data_list:
            continue
        else:
            counter = counter + 1
            print(val)
else:
    sys.exit("Please check the file extensions. First file should be .fasta and second file should be .txt ")