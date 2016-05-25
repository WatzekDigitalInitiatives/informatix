# -*- coding: utf-8 -*-
"""
@author: thatbudakguy
"""

import sys
import bioio
import biomath

# strip file extension and read file
input_txt_name = sys.argv[-1][:-4]
input_txt_data = bioio.readTXT(sys.argv[-1])

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

# write the resulting file
bioio.writeTXT(output_txt_name,output_data)
