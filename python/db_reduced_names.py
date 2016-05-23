# -*- coding: utf-8 -*-
"""
Created on Thu May 19 15:50:11 2016

@author: rishijavia
"""
import sys

if len(sys.argv) != 3:
    sys.exit("Please run the file as python db_reduced_names.py database.fasta names.txt")

if sys.argv[-2].endswith('.fasta') and sys.argv[-1].endswith('.txt'):
    input_db_name = sys.argv[-2]
    with open(input_db_name, 'r') as f:
             data = f.read().splitlines()
    
    print("Database Loaded")
    
    #Name of the seq ids goes in quotes, do not include .txt, just the name of the file
    input_seq_name = sys.argv[-1]
    with open(input_seq_name, 'r') as f:
             seqid = f.read().splitlines() 
    
    print("SeqId Loaded")
    
    output = ""
    
    total = float(len(data))
    
    for i in range(0, len(data), 2):
        id = data[i][1:]
        if id in seqid:
        	print (str(round(((i/total)*100),2))+" % processed \n" + id)
            output = output + data[i]+"\n" + data[i+1]+"\n"
    
    #Name of the output file goes in quotes, do not include .fasta, just the name of the file
    input_db_name = input_db_name[:-6]
    output_file_name = input_db_name+"_concatenated.fasta"
    with open(output_file_name, "w") as file:
        file.write(output)
    
    print("Process complete, output in file "+output_file_name)

else:
    sys.exit("Please check the file extensions. First file should be .fasta and second file should be .txt ")
