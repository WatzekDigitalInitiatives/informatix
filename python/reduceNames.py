# -*- coding: utf-8 -*-
"""
@author: thatbudakguy
"""

import sys
import bioio
import biomath

# strip file extensions and read files
input_txt_name = sys.argv[-1][:-4]
input_txt_data = bioio.trimGreaterThans(bioio.readTXT(sys.argv[-1]))
input_fasta_name = sys.argv[-2][:-6]
input_fasta_data = bioio.trimGreaterThans(bioio.readFASTA(sys.argv[-2]))
input_fasta_splitdata = bioio.splitFASTA(input_fasta_data)
input_fasta_seq_ids = input_fasta_splitdata['output_seq_ids']
input_fasta_seqs = input_fasta_splitdata['output_seqs']

# compare input files to find missing lines
output_fasta_data = biomath.reduceNames(input_txt_data,input_fasta_seq_ids,input_fasta_seqs)
output_seq_ids = output_fasta_data['output_seq_ids']
output_seqs = output_fasta_data['output_seqs']

# define names of the resulting files
output_fasta_name = input_fasta_name+"_concatenated.fasta"

# write the missing lines to a file
bioio.writeFASTA(output_fasta_name,output_seq_ids,output_seqs)
