# workout-processor.py
if __name__ == "__main__":
    # imports
    import sys
    import pandas as pd

    # take argv[1] filename

    # function to determine file type

    # read() function that takes file according to type starts parsing process

    # check() function to check that data in file is valid workout program and syntax is correct

    # import_data() function that takes the data and fills data into pandas dataframe

    # publish() function that fills data from dataframe into html file
    data = pd.read_excel(sys.argv[1], index_col=0)
    print(data)
