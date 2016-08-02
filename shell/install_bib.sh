#!/bin/bash
# install BiB (bioinformatics brew) tool and dependencies
sudo apt-get install -y git build-essential python \
  gcc-4.8 g++-4.8 cmake curl git unzip \
  default-jre-headless libncurses5-dev zlib1g-dev
bash -c "$(curl -fsSL https://bitbucket.org/mhowison/bib/raw/master/install.sh)"
echo "export PATH=/opt/bib/active/bin:$PATH" >>~/.profile
