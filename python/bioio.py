# -*- coding: utf-8 -*-
"""
@author: thatbudakguy
"""

#
# READ
#

# takes input_file and returns rows as input_data
def readCSV(input_file):
    import csv
    with open(input_file, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        input_data = [r for r in reader]
    return input_data

# takes input_file and returns lines as input_data
def readTXT(input_file):
    with open(input_file, 'r') as f:
        input_data = f.read.splitlines()
    return input_data

# takes input_file, strips > chars and returns lines as input_data
def readFASTA(input_file):
    with open(input_file, 'r') as f:
        data = f.read.splitlines()
        for i in data:
            input_data.append(data[i][1:])
    return input_data

#
# MANIPULATE
#

# takes output of readCSV() and returns dict with seqs and seq ids
def splitCSV(input_data):
    output_seq_ids = []
    output_seqs = []
    for data in input_data:
        output_seq_ids.append(data[0])
        output_seqs.append(data[1])
    return {'output_seq_ids':output_seq_ids,'output_seqs':output_seqs}

# takes output of readFASTA() and returns dict with seqs and seq ids
def splitFASTA(input_data):
    output_seq_ids = []
    output_seqs = []
    for i in range(0, len(data), 2):
        output_seq_ids.append(input_data[i])
    for i in range(1, len(data), 2):
        output_seqs.append(input_data[i])
    return {'output_seq_ids':output_seq_ids,'output_seqs':output_seqs}

#
# WRITE
#

# writes csv file with name output_csv_name and data output_csv
def writeCSV(output_csv_name,output_csv):
    import csv
    with open(output_csv_name, "w") as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerows(output_csv)
    print "Wrote " + output_csv_name + "\n"

# writes txt file with name output_txt_name and data output_txt
def writeTXT(output_txt_name,output_txt):
    with open(output_txt_name, "w") as file:
        for line in output_txt:
            file.write(line+"\n")
    print "Wrote " + output_txt_name + "\n"

# writes fasta file with name output_fasta_name and paired output_seq_ids / output_seqs
def writeFASTA(output_fasta_name,output_seq_ids,output_seqs):
    with open(output_fasta_name, "w") as file:
        for i in range(len(output_seqs)):
            file.write(">"+output_seq_ids[i]+"\n")
            file.write(output_seqs[i]+"\n")
    print "Wrote " + output_fasta_name + "\n"
