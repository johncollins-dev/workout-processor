# workout-processor devnotes

## Purpose
This program's purpose is to accept as input training programs as .xlsx files from my work drive
and ouput html files that present the training program and renditions of the workouts. The end goal
is to provide a more human readable and presentable representation of the workout programs I make
for clients while adding no extra work on top of the workout programming I do in google sheets.

## Control Flow
user runs workout-processor on a file
the program must check for:
- [x] lack of argument provided
- [x] too many arguments provided
- [x] that the file exists
- [x] that the file is in an accepted format
Once the file is verified as existing and in an acceptable format, it must be:
- [ ] opened (using openpyxl for xlsx first)
- [ ] checked for syntax (title, date, blocks, notes)
- [ ] checked for data validity
- [ ] read in to a dataframe

Definition of "syntax"
- an xlsx training program consists of one or more sheets
- an xlsx training program period is a sheet starting with "Week" followed by a number
- an xlsx training program period contains 1 or more workouts
- a workout starts with a cell Containing Day followed by a number in bold
- a workout ends with a date in mm/dd/yyyy format on the same row as day
- the row below Day should start with "Exercise" followed by at least 1 column containing "Set"
  followed by a number
  
Tree Structure:
- Training Program
    - Period (1 or more)
        - Workout (1 or more)
            - Block (1 or more)
                - Exercise (1 or more)
## notes
- the most convenient use for workout processor is running the command
  "workout-processor 4-15-26.xlsx" with an appended workout sheet to convert it into a human
  readable html file while retaining all the data
- the name "workout-processor" is not descriptive or makes it clear what its trying to do.
  something like workout-to-html might be more suitable
- John Roberts advocated for test-driven development. I should at least make tests for methods soon
after they are written

So far, I've had to install the following python libraries:
- dev-python/openpyxl (pure python reader and writer of Excel OpenXML files)
- dev-python/pandas (powerful data structures for data analysis and statistics)
- dev-python/pytest (unit testing framework)

## Functions
### validate_file(filename)
- checks if the path exists
### get_extension(filename)
- checks if the extension is accepted, then returns it

