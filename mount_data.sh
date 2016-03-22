# !/bin/bash
# format, mount, and set permissions for 'DATA' external 60GB drive
sleep 30
sudo mkfs.ext4 /dev/xvdb
sudo mkdir /data
sudo mount /dev/xvdb /data
sudo chown -R ubuntu:ubuntu /data
sleep 30
