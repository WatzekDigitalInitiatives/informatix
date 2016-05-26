# !/bin/bash
if [ "${TRAVIS_PULL_REQUEST}" = "false" ]
	then
		packer build bio_base.json # only build an AMI on commits to master
	else
		cd python/test &&	python unittests.py # run unit tests if it's a pull request instead
fi
