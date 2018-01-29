#!/bin/bash

git pull --recurse-submodules

java -cp bin/ili2c.jar ch.interlis.ili2c.MakeIliModelsXml LADM_COL

rm html/ilimodels.xml | true
cp LADM_COL/ilimodels.xml html

rm -r html/LADM_COL | true
mkdir html/LADM_COL
cp LADM_COL/*.ili html/LADM_COL

./generate.py
