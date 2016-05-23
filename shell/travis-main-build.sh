# !/bin/bash
set -ev # break script on nonzero exit code, ending build. also return verbose bash output.
# run tests on our python scripts

# if we're not a pull request check, also build the AMI
if [ "${TRAVIS_PULL_REQUEST}" = "false" ]; then
	packer build bio_base.json
fi
