import sys
import os
sys.path.append(os.path.join(sys.path[0],'lib'))
sys.path.append(os.path.join(sys.path[0],'test'))
import bioio
import biomath

# read input file
read_fasta = bioio.readFASTA([sys.argv[-1]])
input_fasta_name = sys.argv[-1][:-6]
input_fasta_data = read_fasta[input_fasta_name]

# split fasta
input_fasta_splitdata = bioio.splitFASTA(input_fasta_data)
input_fasta_seq_ids = input_fasta_splitdata['output_seq_ids']
input_fasta_seqs = input_fasta_splitdata['output_seqs']

# trim seqids
output_fasta_seq_ids = bioio.trimPepSeqIds(input_fasta_seq_ids)

# recombine and write id prefix files
output_fasta_data = bioio.knitFASTA(output_fasta_seq_ids, input_fasta_seqs)
prefixList = ["ARC", "DRY", "LRE", "PER", "LRU", "PHO", "SIC", "LSP", "PLE", "SCY", "LAZ"]
for prefix in prefixList:
    bioio.splitOnIDPrefix(output_fasta_data, prefix)
