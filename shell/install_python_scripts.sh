#!/bin/bash
# add in @rishijavia's python scripts so they are available to the instance
cd ~ && mkdir scripts && cd scripts
git init && git remote add -f origin https://github.com/WatzekDigitalInitiatives/informatix # links but doesn't clone
git config core.sparsecheckout true # allows us to check out a subfolder of the repo
echo "python/*" >> .git/info/sparse-checkout # we whitelist the python/ subfolder to clone
git pull --depth=1 origin master # shallow clone doesn't pull down repo history, as we don't need it
