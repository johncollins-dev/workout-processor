# workout-xlsx2html
workout-xlsx2html generates an html representation of a training program from its .xlsx file

## Overview
An .xlsx training program gets passed to workout_processor.py where its data gets read in by the reader. The builder then takes that read-in data and populates the data structures. Finally, the data gets passed to the printer which generates html files from templates. The final output is a static html representation of the whole training program.

## Usage
### Running Tests
python -m pytest tests/*

