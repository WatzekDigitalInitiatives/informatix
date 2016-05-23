# !/bin/bash
set -ev # break script on nonzero exit code, ending build. also return verbose bash output.
if [ "${TRAVIS_PULL_REQUEST}" = "false" ]; then
	packer build bio_base.json
fi
