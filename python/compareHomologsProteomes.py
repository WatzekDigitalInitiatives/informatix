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

# strip file extensions and read files
input_1 = sys.argv[-2]
input_2 = sys.argv[-1]
read_fasta_homologs = bioio.readFASTA([input_2])
input_homologs_fasta_name = input_2[:-6]
input_homologs_fasta_data = read_fasta_homologs[input_homologs_fasta_name]
input_homologs_fasta_seq_ids = bioio.splitFASTA(input_homologs_fasta_data)['output_seq_ids']
read_fasta_proteomes = bioio.readFASTA([input_1])
input_proteomes_fasta_name = input_1[:-6]
input_proteomes_fasta_data = read_fasta_proteomes[input_proteomes_fasta_name]
input_proteomes_fasta_seq_ids = bioio.splitFASTA(input_proteomes_fasta_data)['output_seq_ids']

# strip venom codes from proteomes
input_proteomes_fasta_seq_ids = bioio.trimVenomCodes(input_proteomes_fasta_seq_ids)
print input_homologs_fasta_seq_ids

# compare input files to find missing and matching lines
output_seq_ids_match = biomath.findMatchingSeqs(input_homologs_fasta_seq_ids,input_proteomes_fasta_seq_ids)
output_seq_ids_miss = biomath.findMissingSeqs(input_homologs_fasta_seq_ids,input_proteomes_fasta_seq_ids)

# define names of the resulting files
output_txt_name_match = input_homologs_fasta_name+"_matching.txt"
output_txt_name_miss = input_homologs_fasta_name+"_missing.txt"

# write the missing and matching lines to a file
bioio.writeTXT(output_txt_name_match,output_seq_ids_match)
bioio.writeTXT(output_txt_name_miss,output_seq_ids_miss)
