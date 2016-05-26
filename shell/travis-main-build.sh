# !/bin/bash
set -ev # break script on nonzero exit code, ending build. also return verbose bash output.
python --version
python import sys, os
python sys.path.append(os.path.dirname(sys.path[o]),'lib')
python sys.path.append(os.path.dirname(sys.path[o]),'test')
python python/test/unittests.py
if [ "${TRAVIS_PULL_REQUEST}" = "false" ]; then # only build an AMI if we're a commit, not a PR
	packer build bio_base.json
fi
