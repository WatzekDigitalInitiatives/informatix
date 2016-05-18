# !/bin/bash
# update ubuntu and all bio tools
sleep 3
sudo apt-get -y update && sudo apt-get -y upgrade
sudo pip install agalma --upgrade
