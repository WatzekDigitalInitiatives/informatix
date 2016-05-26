# !/bin/bash
if [ "${TRAVIS_PULL_REQUEST}" = "false" ]
	then
    # install unzip
    sudo apt-get install -y unzip
    # install packer on travis machine to build ami
    cd ~ && wget https://releases.hashicorp.com/packer/0.10.1/packer_0.10.1_linux_amd64.zip && chmod 777 packer_0.10.1_linux_amd64.zip
    unzip packer_0.10.1_linux_amd64.zip && sudo cp packer /usr/bin/
fi
