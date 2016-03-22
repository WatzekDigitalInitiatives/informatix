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
