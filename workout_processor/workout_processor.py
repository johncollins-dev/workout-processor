# workout_processor.py

# imports
import sys
from pathlib import Path
import pandas as pd
import pdb
from config import ACCEPTED_EXTENSIONS

def validate_file(filename):
    p = Path(filename)
    if not (p.is_file()):
        raise FileNotFoundError
    return True

def check_extension(filename):
    extension = Path(filename).suffix
    if extension not in ACCEPTED_EXTENSIONS:
        # raise a custom exception
        print("Extension not accepted")

    return extension

# run() function that basically just keeps main clean
def run(input_file):
    validate_file(input_file)
    check_extension(Path(input_file))

# read() function that takes file according to type starts parsing process

# check() function to check that data in file is valid workout program and syntax is correct

# import_data() function that takes the data and fills data into pandas dataframe

# publish() function that fills data from dataframe into html file

# TODO: If no file is passed as command line argument, print usage message
if __name__ == "__main__":
    if len(sys.argv) != 2:
        # print usage message, exit
        print("Incorrect Usage")

    run(sys.argv[1])
    #data = pd.read_excel(sys.argv[1], index_col=0)
    #print(data)
