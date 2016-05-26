# -*- coding: utf-8 -*-
"""
@author: thatbudakguy
"""

import sys
import bioio
import biomath

# strip file extensions and read files
read_txt = bioio.readTXT(sys.argv[-1])
input_txt_name = sys.argv[-1][:-4]
input_txt_data = read_txt[input_txt_name]
read_fasta = bioio.readFASTA(sys.argv[-2])
input_fasta_name = sys.argv[-2][:-6]
input_fasta_data = read_fasta[input_fasta_name]
input_fasta_seq_ids = bioio.splitFASTA(input_fasta_data)['output_seq_ids']

# compare input files to find missing lines
output_seq_ids = biomath.findMissingSeqs(input_txt_data,input_fasta_seq_ids)

# define names of the resulting files
output_txt_name = input_txt_name+"_missing.txt"

# write the missing lines to a file
bioio.writeTXT(output_txt_name,output_seq_ids)
