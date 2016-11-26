#!/usr/bin/python3

pip --version
mkdir local_lib
python3 -m venv local_lib
source local_lib/bin/activate
pip install --upgrade pip
# pip install path.py > install.txt # autre choix
pip install git+https://github.com/jaraco/path.py.git > install.log
python3 my_program.py 
