'''
reader.py
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

def read(filename):
    wb = load_workbook(filename)
    sheet = wb.active

    for sheet in wb.worksheets:
        if(sheet.title.startswith('Week')):
            read_sheet(sheet)

def read_sheet(sheet):
    if(check_title(sheet.cell(row=1,column=1))):
        read_workout(sheet.cell(row=1,column=1))
    # iterate cells row by row until two consecutive cells with no value are found

def read_workout(cell):
    while(cell.fill.start_color.index == 'FF000000')

    print(cell.value)
    # start at provided cell
    # iterate through rows and columns of singular workouts
    # record data to list/dict
    # return list/dict

