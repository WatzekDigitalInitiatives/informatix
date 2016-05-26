# !/bin/bash
set -ev # break script on nonzero exit code, ending build. also return verbose bash output.
python --version
python python/test/unittests.py
if [ "${TRAVIS_PULL_REQUEST}" = "false" ]; then # only build an AMI if we're a commit, not a PR
	packer build bio_base.json
fi
