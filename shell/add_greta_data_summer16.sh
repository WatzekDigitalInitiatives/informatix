#!/bin/bash
# download greta's data and build a new blast database from it
cd /blast/blastdb_custom/
wget #link to db file
makeblastdb -in ComboDatabase2.fasta -dbtype 'prot' -out illumina_cDNA_smd
