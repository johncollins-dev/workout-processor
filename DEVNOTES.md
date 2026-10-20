# workout-processor devnotes

## TODO
1. Address how stretch holds are implemented in line dataclass (ex. 30s Hold)
2. Decide whether a toString method should be employed for dataclasses.

## Purpose
Like a XLSX2HTML program for my workout sheets
This program's purpose is to accept as input training programs as .xlsx files from my work drive
and ouput html files that present the training program and renditions of the workouts. The end goal
is to provide a more human readable and presentable representation of the workout programs I make
for clients while adding no extra work on top of the workout programming I do in google sheets.

## Structure
- workout_processor.py - main driver of the program, is a CLI app
- data.py - defines the necessary data structures needed to take in training program information
- config.py - contains default configuration for the program
- reader.py - takes an input file and reads in the data using openpyxl
- builder.py - builds a training program start to finish
- printer.py - prints a workout program to HTML using jinja2

### Training Program Structure
- Program
    * Period (ex. Macro, Meso, Micro)
        - Workout
            * Block (ex. warmup, activation, skills, strength)
                - Line (1 Exercise, info about sets, rest, etc.)
                    - Exercise
                    - Set

* Programs, Periods, Workouts, Blocks, and Exercises are saveable data that can be used later
* Every datatype above should be a workable/displayable (html) item that can be used without
  interference from the program
* Everything can use default or user specified tags (#strength, #barbell) for easy searching and
  to improve program recommendation

## Inadequacies of Sheets
- not a user friendly experience, especially on mobile
- can be hard to find previously used blocks that I want to copy into other programs
- have to clear out old workouts every once in a while
- links cannot be played within app on mobile

## Lessons learned from workout-processor
- code that is not tested cannot be used. every method/function and file must have tests and they
  must be specific to what they are testing. Recall test-driven development from John Robert's
  class
- if you're going to hardcode, dont make your hardcoded code scalable or maintainable. Lean into
  the hardcodedness fully and don't waste time and effort trying to make it something its not and
  will never be.
- XLSX-workouts2HTML or something like that would have been a better name than "workout-processor"
- whenever youre scanning through some 2d data structure, you usually want nested loops, use while
  loops if you don't know the dimensions, for if you do
- when using openpyxl and reading a sheet in readonly=true mode, you might get the error
  "AttributeError: 'EmptyCell' object has no attribute 'column'". This is because openpyxl creates
  EmptyCells to maintain row and column alignment in a sheet and they do not contain column or row
  data
- dont let your DEVNOTES.md swell with info, trim out the unnecessary information and keep the file
  lean just like Claude.md

## Workout Program Standard Format
General program implementation criteria
- Should not follow specific "schools" of programming such as IOM with unfamiliar terminology (4Q)
- Should be simple
- Ultimate shape of programs/workouts up to the user
    - if a user wants to throw in a list of exercises in a workout, they should be able to

## Future Considerations
- End result of these programs is creating the "Canvas" of gyms. This software should be easy for
  businesses to implement and run and attach their own branding.
    * Look at what strengthportal tried to do and why they seemingly "Failed"
- Workout format accounts for supersets too
- use an open model like llama to train custom llm for domain-specific knowledge of fitness
  training. Automate programming and provide reliable information to coaches and clients.

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

## Class Notes
### data.py
- have to be careful with list instance variables in dataclasses, must use **default_factory** so
  that instances of class don't all use the same list in memory
- in python, class attributes without default values MUST come BEFORE attributes with defaults ex:

OK:
@dataclass
class Line:
    exercise: Exercise
    cells: list[Cell] = field(default_factory=list)
NOT OK:
@dataclass
class Line:
    cells: list[Cell] = field(default_factory=list)
    exercise: Exercise

- when instantiating a dataclass, variables without defaults are considered  required when inputing
  parameters
- when setting an instance variable type to the class being defined, use a   forward reference
  instead of trying to create it while its still being defined
- set the default to NONE when using a class as an instance variable then
  account for it in your code later

### workout-processor
- CLI program that ties the reader, builder, and printer together

### reader.py
- uses openpyxl to open and read in an xlsx file
- to find a workout layer, reader looks for a black background, white foreground, bold text
- can assume that workouts read in will always be the same syntax (google sheets style)
    * otherwise throw error
- get_num_sheets - returns int value for # of sheets
- read_sheet - returns list of dictionaries, where the list is rows and the dictionaries KV pairs
               of cells and their column
    * Only reads rows and columns with data, skips empty rows and columns
    * workouts are entered into the list/dictionary back-to-back
    * Scans dimensions of workouts
        - looks for Cell containing word **Day** with black background/white foreground/bold text.
        - then scans columns until first cell that is empty
        - once workout width is found, it iterates through rows copying column data to list/dict
        - empty rows are omitted but empty cells that are after/between occupied cells are kept
        - loop stops after first empty row coming after "Coaching Notes" is found
        - the reader then goes back to the empty cell found immediately after the end of the black
          columns

- read_workout_next(string) - returns string of first workout found in string, used with read_sheet
- Sheets and workouts maybe should be iterable.

### builder.py
- provides functions to populate dataclasses in data.py with fitness information
### printer.py
- accesses dataclasses and prints them to html templates through jinja2
- anything that makes workout data more readable/presentable belongs in printer

as I work on printer, I'm wondering if keeping the string representation for each line that
    reader spits out would be useful data to keep in the line data structure. Something like
    str_representation that printer could take directly and print without accessing all those
    values again
### editor.py
- curses program that immitates google sheets data input
- also provides webui for building workout programs which can be used by reader and printer
