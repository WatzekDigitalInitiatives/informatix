# -*- coding: utf-8 -*-
"""
@author: thatbudakguy
"""

import sys
import bioio
import biomath

#first cli argument should be the python file and second should be the database names followed by all the VenomCode files
files = sys.argv[2:]
output_file_names = []

for file in files:
	# strip file extension and read file
	input_txt_name = file[:-4]
	input_txt_data = bioio.readTXT(file)

	# add greaterthans
	output_data = bioio.addGreaterThans(input_txt_data)

	# split on greaterthans
	output_data = bioio.splitLinearSeqids(output_data)

	# add venom codes based on filename
	output_data = bioio.addVenomCode(output_data,input_txt_name)

	# replace s??? codes with sample info code
	output_data = bioio.replaceSCodes(output_data)

	# define names of the resulting file
	output_txt_name = input_txt_name+"_proteome_ready.txt"
	output_file_names.append(output_txt_name)

	# write the resulting file
	bioio.writeTXT(output_txt_name,output_data)

output_data = bioio.combineFASTA(output_file_names)
bioio.writeTXT("combined_proteome_db.txt",output_data)

# strip file extensions and read and manipulate files
input_txt_data = bioio.trimVenomCodes(bioio.trimGreaterThans(bioio.readTXT("combined_proteome_db.txt")))
input_fasta_name = sys.argv[1][:-6]
input_fasta_data = bioio.readFASTA(sys.argv[1])
input_fasta_splitdata = bioio.splitFASTA(input_fasta_data)
input_fasta_seq_ids = input_fasta_splitdata['output_seq_ids']
input_fasta_seqs = input_fasta_splitdata['output_seqs']

# compare input files to find missing lines
output_fasta_data = biomath.reduceNames(input_txt_data,input_fasta_seq_ids,input_fasta_seqs)
output_seq_ids = output_fasta_data['output_seq_ids']
output_seqs = output_fasta_data['output_seqs']

# define names of the resulting files
output_fasta_name = input_fasta_name+".fasta"

# write the missing lines to a file
bioio.writeFASTA(output_fasta_name,output_seq_ids,output_seqs)