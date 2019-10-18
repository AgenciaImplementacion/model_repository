#!/bin/bash

# rationale: update submodules
#git submodule update --recursive --init
# rationale: previous update isn't working if commit was deleted
# link: https://stackoverflow.com/questions/5828324/update-git-submodule-to-latest-commit-on-origin
git submodule foreach git pull origin master
git submodule update --recursive --init

# rationale: remove path of models and pull from LADM_COL repository
rm -rf html/LADM_COL | true
find LADM_COL/ -name '*.ili' -exec cp --parents \{\} html \;

# rationale: remove and recreate ilimodels.xml
rm html/ilimodels.xml | true
java -cp bin/ili2c.jar ch.interlis.ili2c.MakeIliModelsXml html

#Install requirements
pip3.4 install -r requirements.txt
# rationale: generate 'index.html' of all paths with .ili files using templates
./generate.py
