'''
reader.py
shamelessly hardcoded to read only my personal workout spreadsheets

TODO:
create tests for get_workout_width
'''
from openpyxl import load_workbook

# checks if cell has black bg, bold, and starts with 'Day'
def check_title(cell):
    if cell.value is not None:
        return cell.value.startswith('Day') and cell.font.bold and cell.fill.start_color.index == 'FF000000'

    return False


# checks if a cell is empty and unused
# these cells are not part of any workout grid and can be skipped over
# two in a row will signify the end of a row of workouts
def check_unused(cell):
    if cell.value is not None:
        return False

    fill = cell.fill

    if fill is None:
        return True

    color = fill.start_color

    return color.rgb in (None, '00000000', 'FFFFFFFF')

def check_coaching_notes(cell):
    return cell.value == 'Coaching Notes'

def read(filename):
    wb = load_workbook(filename, read_only=True)
    sheet = wb.active

    for sheet in wb.worksheets:
        if(sheet.title.startswith('Week')):
            read_sheet(sheet)

def get_workout_width(sheet, cell):
    width = 1
    c = cell.column
    r = cell.row
    while(sheet.cell(row=r,column=c).is_date == False):
        c += 1
        width += 1

    return width

def get_workout_height(sheet, cell):
    height = 1
    c = cell.column
    r = cell.row
    while(check_coaching_notes(sheet.cell(row=r,column=c)) == False):
        r += 1
        height += 1

    return height + 1 # the + 1 is to account for the merged cell directly beneath Coaching Notes
# which is part of the workout section

def read_sheet(sheet):
    consecutive_unused = 0
    x = 1
    y = 1

    current_workout_w = 1
    current_workout_h = 1

    while(consecutive_unused < 2):
        current_cell = sheet.cell(row=x,column=y)
        
        if(check_title(current_cell)):
            current_workout_w = get_workout_width(sheet, current_cell)
            current_workout_h = get_workout_height(sheet, current_cell)
            read_workout(sheet, current_cell, current_workout_w, current_workout_h)
            y += current_workout_w
            consecutive_unused = 0

        elif(check_unused(current_cell)):
            consecutive_unused += 1
            y += 1

def read_workout(sheet, cell, w, h):
    print('Hi!')
    #while(cell.fill.start_color.index == 'FF000000')
    #print(cell.value)
    # start at provided cell
    # iterate through rows and columns of singular workouts
    # record data to list/dict
    # return list/dict

