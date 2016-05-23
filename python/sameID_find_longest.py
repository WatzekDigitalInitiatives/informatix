# -*- coding: utf-8 -*-
"""
Created on Thu May 19 13:42:18 2016

@author: rishijavia
"""
import csv
import sys

input_csv = sys.argv[-1]
if len(sys.argv) != 2:
    sys.exit("Please run the file as python sameID_find_longest.py blast_output.csv")
    
if sys.argv[-1].endswith('.csv'):
    
    with open(input_csv, 'r') as f:
             reader = csv.reader(f, delimiter=',')
             next(reader)
             rows = [r for r in reader]
    
    data = rows[0]
    
    output_data = []
    
    for i in range(1,len(rows)):
        col1 = rows[i][0]
        if (col1 == data[0]):
            len_data = len(data[1])
            len_test = len(rows[i][1])
            if(len_test > len_data):
                data = rows[i]
        else:
            output_data.append(data)
            data = rows[i]
    
    #You can change the value of output_file_name to the name of the output file you want
    input_csv = input_csv[:-4]
    output_file_name = input_csv+"_trimmed"
    with open(output_file_name+".csv", "w") as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerows(output_data)
    
    seq_id = []
    seq = []
    for data in output_data:
        seq_id.append(data[0])
        seq.append(data[1])
    
    with open(output_file_name+"_names_only"+".txt", "w") as file:
        for id in seq_id:
            file.write(id+"\n")
    
    with open(output_file_name+".fasta", "w") as file:
        for i in range(len(seq)):
            file.write(">"+seq_id[i]+"\n")
            file.write(seq[i]+"\n")
    print("Output file names: \n"+output_file_name+".csv \n"+output_file_name+"_names_only.txt \n"+output_file_name+".fasta \n")

else:
    sys.exit("Please check the file extensions. The input file should be a .csv file")