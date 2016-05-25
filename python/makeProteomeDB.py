# -*- coding: utf-8 -*-
"""
@author: thatbudakguy
"""

import sys
import bioio
import biomath

files = sys.argv[1:]
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