# Steps
1. Create data types outlined in data.md that can hold anything in a training program
2. Basic CLI program that asks for input spreadsheet or manual entry of workout/program details
    - print welcome screen "workout-processor-v0.1" "1. to restart" "2. to quit"
    - while loop
    - line that waits for user input
    - loop iterates as long as user input is not 1 or 2

## notes
- the most convenient use for workout processor is running the command
  "workout-processor 4-15-26.xlsx" with an appended workout sheet to convert it into a human
  readable html file while retaining all the data

So far, I've had to install the following python libraries:
- dev-python/openpyxl (pure python reader and writer of Excel OpenXML files)
- dev-python/pandas (powerful data structures for data analysis and statistics)
- dev-python/pytest (unit testing framework)

## Functions
### validate_file(filename)
- checks if the path exists
### get_extension(filename)
- checks if the extension is accepted, then returns it
