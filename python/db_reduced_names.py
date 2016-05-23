# -*- coding: utf-8 -*-
"""
Created on Thu May 19 15:50:11 2016

@author: rishijavia
"""
import sys
from biomath import reduceNames

if len(sys.argv) != 3:
    sys.exit("Please run the file as python db_reduced_names.py database.fasta names.txt")

if sys.argv[-2].endswith('.fasta') and sys.argv[-1].endswith('.txt'):
    input_db_name = sys.argv[-2]
    with open(input_db_name, 'r') as f:
             data = f.read().splitlines()
    
    print("Database Loaded")
    
    input_seq_name = sys.argv[-1]
    with open(input_seq_name, 'r') as f:
             seqid = f.read().splitlines() 
    
    print("SeqId Loaded")
    
    output = reduceNames(seqid, data)
    output_string = ""
    for seqid, seq in output.items():
        output_string = output_string + seqid+"\n" + seq+"\n"    
    
    input_db_name = input_db_name[:-6]
    output_file_name = input_db_name+"_concatenated.fasta"
    with open(output_file_name, "w") as file:
        file.write(output_string)
    
    print("Process complete, output in file "+output_file_name)

else:
    sys.exit("Please check the file extensions. First file should be .fasta and second file should be .txt ")
