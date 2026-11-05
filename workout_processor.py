# workout_processor.py

# imports
import sys
from pathlib import Path
import pandas as pd
import pdb
from config import ACCEPTED_EXTENSIONS
from data.data import Exercise, Muscle, Equipment, Adaptation, Movement, Tag
from reader import read
from builder import build_set, build_tag, build_exercise, build_line
from printer import Printer

USAGE_MESSAGE = "usage: workout-processor 'Exercise Program.xlsx"

# returns true if the filename is a File that exists
def validate_file(filename):
    p = Path(filename)
    if not (p.is_file()):
        raise FileNotFoundError
    return True

# returns the file extension of filename
def check_extension(filename):
    extension = Path(filename).suffix
    if extension not in ACCEPTED_EXTENSIONS:
        # raise a custom exception
        print("Extension not accepted")

    return extension

# run() function that basically just keeps main clean
def run(input_file):
    validate_file(input_file)
    if(check_extension(Path(input_file)) == '.xlsx'):
        print("The program recognizes the file as .xlsx")

if __name__ == "__main__":
    #sample1 = Path.cwd() / "tests" / "samples" / "Sample 1.xlsx"
    #sample2 = Path.cwd() / "tests" / "samples" / "Sample 2.xlsx"
    #sample3 = Path.cwd() / "tests" / "samples" / "Sample 3.xlsx"
    #sample4 = Path.cwd() / "tests" / "samples" / "Sample 4.xlsx"
    #if len(sys.argv) != 2:
    #    print(USAGE_MESSAGE)

    #run(sys.argv[1])
    #data = pd.read_excel(sys.argv[1], index_col=0)
    #print(data)
    #read(sample1)

    # ad hoc test for printer
    exercise = build_exercise('BB Back Squat', '', '', '', '')
    sets = [
            build_set('Set 1', 8, 40.0, 0.0, 'slow', 0),
            build_set('Set 2', 8, 50.0, 0.0, 'slow', 1),
            build_set('Set 3', 6, 60.0, 0.0, 'slow', 2),
            build_set('Set 4', 6, 80.0, 0.0, 'slow', 3)
    ]
    tags = [
            build_tag('quads'),
            build_tag('squat')
    ]
    line = build_line(30, 0, exercise, sets)
    Printer(line).write("line.html")
