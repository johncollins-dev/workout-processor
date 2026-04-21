# workout-processor.py

# imports
import sys
from pathlib import Path
import pandas as pd
import pdb
import pytest

# function to determine file type
# TODO: check that the input provided is valid path, if not throw error
def validate_file(filename):
    p = Path(filename)
    if not (p.is_file()):
        raise FileNotFoundError
    return True

def get_extension(filename: Path):
    accepted_extensions = {'.ods', '.pdf', '.csv', '.xlsx'}
    extension = filename.suffix
    return extension

# run() function that basically just keeps main clean
def run()
    input_file = sys.argv[1]
    validate_file(input_file)
    get_extension(Path(input_file))

# read() function that takes file according to type starts parsing process

# check() function to check that data in file is valid workout program and syntax is correct

# import_data() function that takes the data and fills data into pandas dataframe

# publish() function that fills data from dataframe into html file

# TODO: If no file is passed as command line argument, print usage message
if __name__ == "__main__":
    if len(sys.argv) != 2:
        # print usage message, exit
    run()
    #data = pd.read_excel(sys.argv[1], index_col=0)
    #print(data)
