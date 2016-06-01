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

# strip file extensions,'>' and read files
read_fasta = bioio.readFASTA([sys.argv[-1]])
input_fasta_name = sys.argv[-1][:-6]
input_fasta_data = read_fasta[input_fasta_name]
input_fasta_splitdata = bioio.splitFASTA(input_fasta_data)
input_fasta_seq_ids = input_fasta_splitdata['output_seq_ids']
input_fasta_seqs = input_fasta_splitdata['output_seqs']

# match seqIDs to seqs for easier sorting
matched_fasta = bioio.matchFASTA(input_fasta_seq_ids,input_fasta_seqs)
print matched_fasta
# output_fasta_data = biomath.reduceIsoforms(input_fasta_seq_ids,input_fasta_seqs)
# output_seq_ids = output_fasta_data['output_seq_ids']
# output_seqs = output_fasta_data['output_seqs']

# write the seqs to the file
# output_fasta_name = input_fasta_name+"_singleIsoforms.fasta"
# bioio.writeFASTA(output_fasta_name,output_seq_ids,output_seqs)
