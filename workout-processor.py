# workout-processor.py

# imports
import os
import sys
import pandas as pd

# function to determine file type
# TODO: check that the input provided is valid path, if not throw error
def get_extension(filename):
    file_name, file_extension = os.path.splitext(filename)
    print(file_name)
    print(file_extension)

# read() function that takes file according to type starts parsing process

# check() function to check that data in file is valid workout program and syntax is correct

# import_data() function that takes the data and fills data into pandas dataframe

# publish() function that fills data from dataframe into html file

if __name__ == "__main__":
    get_extension(sys.argv[1])
    #data = pd.read_excel(sys.argv[1], index_col=0)
    #print(data)
