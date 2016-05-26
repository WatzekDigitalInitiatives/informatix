# !/bin/bash
set -ev # break script on nonzero exit code, ending build. also return verbose bash output.
python --version
python python/test/unittests.py
ls -al
ls -al python/
ls -al python/test
if [ "${TRAVIS_PULL_REQUEST}" = "false" ] # only build an AMI if we're a commit, not a PR
	then
		packer build bio_base.json
fi
