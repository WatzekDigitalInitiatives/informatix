# -*- coding: utf-8 -*-
"""
@author: thatbudakguy
"""

import sys
import bioio
import biomath

# strip file extension and read file
input_csv_name = sys.argv[-1][:-4]
input_csv_data = bioio.readCSV(sys.argv[-1])

# find longest sequences and get their corresponding ids
output_csv_data = biomath.findLongestSeq(input_csv_data)
output_seq_ids = bioio.splitCSV(output_csv_data)['output_seq_ids']
output_seqs = bioio.splitCSV(output_csv_data)['output_seqs']

# define names of the resulting files
output_csv_name = input_csv_name+"_trimmed.csv"
output_txt_name = input_csv_name+"_names_only.txt"
output_fasta_name = input_csv_name+".fasta"

# write the resulting data to files
bioio.writeCSV(output_csv_name,output_csv_data)
bioio.writeTXT(output_txt_name,output_seq_ids)
bioio.writeFASTA(output_fasta_name,output_seq_ids,output_seqs)
