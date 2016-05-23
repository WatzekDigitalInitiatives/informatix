# -*- coding: utf-8 -*-
"""
Created on Fri May 20 09:21:00 2016

@author: rishijavia
"""

import sys
from biomath import findMissingSeqs

if len(sys.argv) != 3:
    sys.exit("Please run the file as python find_unavailable_seqid.py database.fasta names.txt")
    
if sys.argv[-2].endswith('.fasta') and sys.argv[-1].endswith('.txt'):
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

    output = findMissingSeqs(names_list, data_list)    
    
    print(output)
else:
    sys.exit("Please check the file extensions. First file should be .fasta and second file should be .txt ")