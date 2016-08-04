# -*- coding: utf-8 -*-
"""
@author: thatbudakguy
"""

import sys
import os
sys.path.append(os.path.join(sys.path[0],'lib'))
sys.path.append(os.path.join(sys.path[0],'test'))
import bioio
import biomath

# strip file extension and read file
read_csv = bioio.readCSV([sys.argv[-1]])
read_fasta = bioio.readFASTA([sys.argv[-2]])
input_fasta_name = sys.argv[-2][:-6]
input_fasta_data = read_fasta[input_fasta_name]
input_fasta_splitdata = bioio.splitFASTA(input_fasta_data)
input_fasta_seq_ids = input_fasta_splitdata['output_seq_ids']
input_fasta_seqs = input_fasta_splitdata['output_seqs']
input_csv_name = sys.argv[-1][:-4]
input_csv_data = read_csv[input_csv_name]

# find longest sequences and get the name list of seq ids
longest_csv_data = biomath.findLongestSeq(input_csv_data)
name_list = bioio.splitCSV(longest_csv_data)['output_seq_ids']

# check name list against the database
output_fasta_data = biomath.reduceNames(name_list,input_fasta_seq_ids,input_fasta_seqs)
output_seq_ids = output_fasta_data['output_seq_ids']
output_seqs = output_fasta_data['output_seqs']

# write results to a file
output_fasta_name = input_csv_name + "_homologs.fasta"
bioio.writeFASTA(output_fasta_name,output_seq_ids,output_seqs)
