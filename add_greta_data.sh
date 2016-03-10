#!/bin/bash
# download greta's data and build a new blast database from it
sleep 30
sudo su
cd /blast/blastdb_custom/
wget http://files.cgrb.oregonstate.edu/CGRB/Kronmiller/downloads/binford20151205/redo_protein_blasts/all_redo_pep.fasta
makeblastdb -in all_redo_pep.fasta -dbtype 'prot' -out greta_db
sleep 30
