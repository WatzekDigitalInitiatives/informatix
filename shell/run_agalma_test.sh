#!/bin/bash
# run part of the agalma tutorial/test
cd /data
mkdir -p agalma/analyses
mkdir -p agalma/data
mkdir -p agalma/scratch
export BIOLITE_RESOURCES="database=$PWD/agalma/biolite.sqlite"
cd agalma/data
agalma testdata
agalma catalog insert --paths SRX288285_1.fq SRX288285_2.fq --species "Agalma elegans" --ncbi_id 316166 --itis_id 51383
export BIOLITE_RESOURCES="$BIOLITE_RESOURCES,threads=50,memory=50G"
cd ../scratch
agalma transcriptome --id HWI-ST625-73-C0JUVACXX-7 --outdir ../analyses
cd ..
agalma report --id HWI-ST625-73-C0JUVACXX-7 --outdir reports/HWI-ST625-73-C0JUVACXX-7
agalma resources --id HWI-ST625-73-C0JUVACXX-7 --outdir reports/HWI-ST625-73-C0JUVACXX-7
export BIOLITE_RESOURCES="$BIOLITE_RESOURCES,outdir=$PWD/analyses,agalma_database=$PWD/agalma.sqlite"
cd data
agalma catalog insert --id SRX288285 --paths SRX288285_1.fq SRX288285_2.fq --species "Agalma elegans" --ncbi_id 316166
agalma catalog insert --id SRX288432 --paths SRX288432_1.fq SRX288432_2.fq --species "Craseoa lathetica" --ncbi_id 316205
agalma catalog insert --id SRX288431 --paths SRX288431_1.fq SRX288431_2.fq --species "Physalia physalis" --ncbi_id 168775
agalma catalog insert --id SRX288430 --paths SRX288430_1.fq SRX288430_2.fq --species "Nanomia bijuga" --ncbi_id 168759
agalma catalog insert --id JGI_NEMVEC --paths JGI_NEMVEC.fa --species "Nematostella vectensis" --ncbi_id 45351
cd ../scratch
agalma postassemble --id SRX288285 --assembly ../data/SRX288285.fa
agalma postassemble --id SRX288430 --assembly ../data/SRX288430.fa
agalma postassemble --id SRX288431 --assembly ../data/SRX288431.fa
agalma postassemble --id SRX288432 --assembly ../data/SRX288432.fa
agalma postassemble --id JGI_NEMVEC --external
