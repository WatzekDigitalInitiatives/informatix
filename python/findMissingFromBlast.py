import sys
import os
sys.path.append(os.path.join(sys.path[0],'lib'))
sys.path.append(os.path.join(sys.path[0],'test'))
import bioio
import biomath

# read input files and names
db_dict = bioio.readFASTAdict([sys.argv[-1]])
input_db_name = sys.argv[-1][:-6]
blast_dict = bioio.readFASTAdict([sys.argv[-2]])
input_blast_name = sys.argv[-2][:-6]

# find missing seqids and seqs
output_data = biomath.findMissingFromDB(db_dict[input_db_name], blast_dict[input_blast_name])

# write results
output_name = input_blast_name + "_missing_from_" + input_db_name + ".fasta"
bioio.writeFASTAdict(output_name, output_data)
