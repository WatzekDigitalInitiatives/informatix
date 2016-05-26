# -*- coding: utf-8 -*-
"""
@author: thatbudakguy
"""

import sys
import bioio
import biomath

# strip file extensions and read files
read_fasta = bioio.readFASTA(sys.argv[1])
input_fasta_name = sys.argv[1][:-6]
input_fasta_data = read_fasta[input_fasta_name]
input_fasta_splitdata = bioio.splitFASTA(input_fasta_data)
input_fasta_seq_ids = input_fasta_splitdata['output_seq_ids']
input_fasta_seqs = input_fasta_splitdata['output_seqs']
read_txt = bioio.readTXT(sys.argv[2:])
output_combined_data = []

# reformat and combine seqid lists
for filename,data in read_txt.iteritems():

	# split on greaterthans
	output_data = bioio.splitLinearSeqids(data)

	# add venom codes based on filename
	output_data = bioio.addVenomCodes(output_data,filename)

	# replace s??? codes with sample info code
	output_data = bioio.replaceSCodes(output_data)

	# write the 'fixed' version of each file
	output_txt_name = filename + "_proteome_ready.txt"
	bioio.writeTXT(output_txt_name,output_data)

	# also append its data to a combined file
	output_combined_data.append(output_data)

# write the combined proteome data file
bioio.writeTXT("combined_proteome_db.txt",output_combined_data)

# call reduceNames to check combined proteomes against database
output_fasta_data = biomath.reduceNames(output_combined_data,input_fasta_seq_ids,input_fasta_seqs,1)
output_seq_ids = output_fasta_data['output_seq_ids']
output_seqs = output_fasta_data['output_seqs']

# write the resulting fasta file
output_fasta_name = input_fasta_name+"_proteomes.fasta"
bioio.writeFASTA(output_fasta_name,output_seq_ids,output_seqs)
