import sys
import os
sys.path.append(os.path.join(sys.path[0],'lib'))
sys.path.append(os.path.join(sys.path[0],'test'))
import bioio
import biomath

read_fasta = bioio.readFASTA([sys.argv[-1]])
input_fasta_name = sys.argv[-1][:-6]
input_fasta_data = read_fasta[input_fasta_name]

prefixList = ["ARC", "DRY", "LRE", "PER"]
for prefix in prefixList:
    bioio.splitOnIDPrefix(input_fasta_data, prefix)
