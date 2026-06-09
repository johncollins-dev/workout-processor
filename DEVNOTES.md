# workout-processor devnotes

## Purpose
Like a XLSX2HTML program for my workout sheets
This program's purpose is to accept as input training programs as .xlsx files from my work drive
and ouput html files that present the training program and renditions of the workouts. The end goal
is to provide a more human readable and presentable representation of the workout programs I make
for clients while adding no extra work on top of the workout programming I do in google sheets.

## Inadequacies of Sheets
- not a user friendly experience, especially on mobile
- can be hard to find previously used blocks that I want to copy into other programs
- have to clear out old workouts every once in a while
- links cannot be played within app on mobile

## Workout Program Standard Format
General program implementation criteria
- Should not follow specific "schools" of programming such as IOM with unfamiliar terminology (4Q)
- Should be simple
- Ultimate shape of programs/workouts up to the user
    - "Periods" and "Blocks" should be optional organizational categories
    - if a user wants to throw in a list of exercises of a workout datatype, they should be able to

### Structure
- Program
    * Period (ex. Macro, Meso, Micro)
        - Workout
            * Block (ex. warmup, activation, skills, strength)
                - Exercise
* Programs, Periods, Workouts, Blocks, and Exercises are saveable data that can be used later
* Every datatype above is optional. Each one should be a workable/displayable (html) item that can
  be used without interference from the program
* Everything can use default or user specified tags (#strength, #barbell) for easy searching and
  to improve program recommendation
* so far, none of these datatypes deal with sets or weights/reps. they are only a way to abstract
  exercises and lists of exercises.

## Future Considerations
- Programs, periods, workouts, blocks could be replaced by arbitrary "layers" that can contain
  exercises or other layers
- There are already human anatomy apis and exercise databases out there. Need to decide on whether
  to use those or create own.
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
