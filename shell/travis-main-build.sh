# !/bin/bash
set -ev # break script on nonzero exit code, ending build. also return verbose bash output.
if [ "${TRAVIS_PULL_REQUEST}" = "false" ] # only build an AMI if we're a commit, not a PR
	then
		packer build bio_base.json
	else
		cd python/test &&	python unittests.py
fi
