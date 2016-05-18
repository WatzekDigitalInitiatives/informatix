#!/bin/bash
# download greta's data and build a new blast database from it
mkdir /data/greta_data
cd /data/greta_data
wget http://library.lclark.edu/testpages/fasta/all_redo_pep.fasta
makeblastdb -in all_redo_pep.fasta -dbtype 'prot' -out greta_db
