# -*- coding: utf-8 -*-
"""
Created on Thu May 19 15:50:11 2016

@author: rishijavia
"""

input_db_name = ""
with open(input_db_name+".fasta", 'r') as f:
         data = f.read().splitlines()

print("Database Loaded")

input_seq_name = ""
with open(input_seq_name+".txt", 'r') as f:
         seqid = f.read().splitlines() 

print("SeqId Loaded")

output = ""

total = float(len(data))

for i in range(0, len(data), 2):
    id = data[i][1:]
    if id in seqid:
    	print (str(round(((i/total)*100),2))+" % processed \n" + id)
        output = output + data[i]+"\n" + data[i+1]+"\n"

output_file_name = "output"
with open(output_file_name+"_concatenated_db"+".fasta", "w") as file:
    file.write(output)

print("Process complete, output in file "+output_file_name+"_concatenated_db"+".fasta")