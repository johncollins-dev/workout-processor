'''
reader.py
'''
from openpyxl import load_workbook

# checks if cell has black bg, bold, and starts with 'Day'
def check_title(cell):
    return cell.value.startswith('Day') and cell.font.bold and cell.fill.start_color.index == 'FF000000'

def read(filename):
    wb = load_workbook(filename)
    ws = wb.active

    # iterate through sheets until 'Week 1' is found
    for sheet in wb.worksheets:
        if (sheet.title.startswith('Week'):
            sheet = wb.active
            read_sheet(sheet)

def read_sheet(sheet):
    if(check_title(sheet.cell(row=1,column=1))):
        read_workout(sheet.cell)

# return data retrieved from workout within a sheet
def read_workout(cell):
    # start at provided cell
    # iterate through rows and columns of singular workouts
    # record data to list/dict
    # return list/dict

