#!/bin/bash
# install CAP3 tool
wget http://seq.cs.iastate.edu/CAP3/cap3.linux.x86_64.tar
tar -xvf cap3.linux.x86_64.tar && cd CAP3/
echo "export PATH=~/CAP3:$PATH" >>~/.profile
