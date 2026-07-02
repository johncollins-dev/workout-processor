'''
reader.py
shamelessly hardcoded to read only my personal workout spreadsheets

TODO:
create tests for get_workout_width
'''
from openpyxl import load_workbook

# checks if cell has black bg, bold, and starts with 'Day'
def check_title(cell):
    return cell.value.startswith('Day') and cell.font.bold and cell.fill.start_color.index == 'FF000000'

# checks if a cell is empty and unused
# these cells are not part of any workout grid and can be skipped over
# two in a row will signify the end of a row of workouts
def check_unused(cell):
    return cell.value == 'None' and cell.fill.start_color.index == '00000000'

def check_coaching_notes(cell):
    return cell.value == 'Coaching Notes'

def read(filename):
    wb = load_workbook(filename, read-only = True)
    sheet = wb.active
    program = []

    for sheet in wb.worksheets:
        if(sheet.title.startswith('Week')):
            program.append(read_sheet(sheet))

    return program

def get_workout_width(sheet, cell):
    width = 1
    c = cell.column
    r = cell.row
    while(sheet.cell(row=r,column=c).is_date == False):
        c += 1;
        width += 1;

    return width

def get_workout_height(sheet, cell):


def read_sheet(sheet):
    sheet_data = []
    consecutive_unused = 0
    x = 1
    y = 1

    while(consecutive_unused < 2):
        current_cell = sheet.cell(row=x,column=y)
        if(check_title(current_cell):
            sheet_data.append(read_workout(sheet, current_cell))
        elif(check_unused(current_cell):
            consecutive_unused += 1

        y += 1

    x += 1
        # iterate cells row by row until two consecutive cells with no value are found

def read_workout(sheet, cell):
    while(cell.fill.start_color.index == 'FF000000')

    print(cell.value)
    # start at provided cell
    # iterate through rows and columns of singular workouts
    # record data to list/dict
    # return list/dict

