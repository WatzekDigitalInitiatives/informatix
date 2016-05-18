#!/bin/bash
# download greta's data and build a new blast database from it
cd /blast/blastdb_custom/
wget http://library.lclark.edu/testpages/fasta/ComboDatabase2.fasta
makeblastdb -in ComboDatabase2.fasta -dbtype 'prot' -out illumina_cDNA_smd
