# -*- coding: utf-8 -*-
"""
Created on Fri May 20 09:21:00 2016

@author: rishijavia
"""

input_db = "concatenated_db"
with open(input_db+".fasta", 'r') as f:
    data = f.read().splitlines()
         
input_names = "SicToxBLAST160517_redcomp_trimmed2_names_only"
with open(input_names+".txt", 'r') as f:
    names = f.read().splitlines()

data_list = []
names_list = names
for i in range(0, len(data), 2):
    data_list.append(data[i][1:])
    
for val in names_list:
    if val in data_list:
        continue
    else:
        counter = counter + 1
        print(val)