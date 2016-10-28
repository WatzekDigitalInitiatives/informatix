# !/bin/bash
if [ "${TRAVIS_PULL_REQUEST}" = "false" ]
	then
    # install unzip and wget if we don't have them
    sudo apt-get install -y unzip wget
    # install packer on travis machine to build ami
    wget https://releases.hashicorp.com/packer/0.10.1/packer_0.10.1_linux_amd64.zip && chmod +x packer_0.10.1_linux_amd64.zip
    unzip packer_0.10.1_linux_amd64.zip
    sudo cp packer /usr/bin/
fi
