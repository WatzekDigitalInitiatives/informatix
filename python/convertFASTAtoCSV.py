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

# strip file extensions and read file
read_fasta = bioio.readFASTA([sys.argv[1]])
input_fasta_name = sys.argv[1][:-6]
input_fasta_data = read_fasta[input_fasta_name]
input_fasta_seq_ids = bioio.splitFASTA(input_fasta_data)['output_seq_ids']
input_fasta_seqs = bioio.splitFASTA(input_fasta_data)['output_seqs']

# reformat as list of lists
output_csv_data = []
for i in range(len(input_fasta_seq_ids)):
	data = []
	data.append(input_fasta_seq_ids[i])
	data.append(input_fasta_seqs[i])
	output_csv_data.append(data)

# write the resulting csv file
output_csv_name = input_fasta_name + ".csv"
bioio.writeCSV(output_csv_name,output_csv_data)
