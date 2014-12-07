[![Documentation Status](https://readthedocs.org/projects/dalton-tools/badge/?version=latest)](https://readthedocs.org/projects/dalton-tools/?badge=latest)
[![Build Status](https://travis-ci.org/fishstamp82/dalton_tools.svg?branch=master)](https://travis-ci.org/fishstamp82/dalton_tools)
[![Coverage Status](https://img.shields.io/coveralls/fishstamp82/dalton_tools.svg)](https://coveralls.io/r/fishstamp82/dalton_tools?branch=master)

pyclasses
=========

Main files used daily is:

read_dal.py
molecules.py


The file 

template.py

contains templates for molecule properties derived analytically for water modeles, and is used by the class
Molecule to add the class Property to all atomic sites to a molecule.

right now only water molecules are implemented.



read_dal.py is used to generate qmmm input files for dalton. Right now used with Water molecules.