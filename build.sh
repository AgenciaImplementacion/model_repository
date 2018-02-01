#!/bin/bash

git submodule update --recursive --init

java -cp bin/ili2c.jar ch.interlis.ili2c.MakeIliModelsXml LADM_COL

rm html/ilimodels.xml | true
mv LADM_COL/ilimodels.xml html

rm -rf html/LADM_COL | true
find LADM_COL/ -name '*.ili' -exec cp --parents \{\} html \;

./generate.py
