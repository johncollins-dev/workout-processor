## notes
- the most convenient use for workout processor is running the command
  "workout-processor 4-15-26.xlsx" with an appended workout sheet to convert it into a human
  readable html file while retaining all the data
- the name "workout-processor" is not descriptive or makes it clear what its trying to do.
  something like workout-to-html might be more suitable


So far, I've had to install the following python libraries:
- dev-python/openpyxl (pure python reader and writer of Excel OpenXML files)
- dev-python/pandas (powerful data structures for data analysis and statistics)
- dev-python/pytest (unit testing framework)

## Functions
### validate_file(filename)
- checks if the path exists
### get_extension(filename)
- checks if the extension is accepted, then returns it

## Flow
user runs workout-processor on a file
the program must check for:
- [x] lack of argument provided
- [x] too many arguments provided
- [x] that the file exists
- [x] that the file is in an accepted format

once that is done, the file must be
- [ ] opened
- [ ] checked for syntax
- [ ] checked for data validity
- [ ] read in to a dataframe
