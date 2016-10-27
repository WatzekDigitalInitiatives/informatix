# -*- coding: utf-8 -*-
"""
@author: thatbudakguy
"""

import sys
import os
sys.path.append(os.path.join(sys.path[0],'lib'))
sys.path.append(os.path.join(sys.path[0],'test'))
import bioio

# strip file extension, read file, reset '>'
read_txt = bioio.readTXT([sys.argv[-1]])
input_txt_name = sys.argv[-1][:-4]
input_txt_data = bioio.addGreaterThans(read_txt[input_txt_name])
output_txt_data = []

# break lines on first instance of a dash
for line in input_txt_data:
    first_dash_index = line.find('-')
    output_txt_data.append(line[:first_dash_index] + '\n' + line[first_dash_index:])

# write the seqs to the file
output_txt_name = input_txt_name + "_clean.txt"
bioio.writeTXT(output_txt_name, output_txt_data)
