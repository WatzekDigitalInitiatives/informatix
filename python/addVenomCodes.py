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

# add venom codes
output_fasta_seq_ids = bioio.addVenomCodes(input_fasta_seq_ids,input_fasta_name)

# write file
output_fasta_name = input_fasta_name + "_vCodes.fasta"
bioio.writeFASTA(output_fasta_name, output_fasta_seq_ids, input_fasta_seqs)
