'''
reader.py
shamelessly hardcoded to read only my personal workout spreadsheets

TODO:
create tests for
- get_workout_width
- get_workout_height
- check_title
- check_unused
- check_coaching_notes

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
    wb.active = 9
    sheet = wb.active

    #temporary measure for testing read_sheet:
    print('reading sheet ', sheet.title)
    read_sheet(sheet)
    #for sheet in wb.worksheets:
    #    if(sheet.title.startswith('Week')):
    #        read_sheet(sheet)

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
    sheet_data = []
    
    x = 1
    y = 1
    pivot_cell = sheet.cell(row=x, column=y)

    blank_count_h = 0
    blank_count_v = 0
    
    # scan sheets vertically
    while(blank_count_v < 2):
        print("iterating v")
        # scan sheets horizontally
        while(blank_count_h < 2):
            print("iterating h")
            if(check_title(pivot_cell)):
                #sheet_data.extend(read_workout(sheet, pivot_cell))
                read_workout(sheet, pivot_cell)
                y += get_workout_width(sheet, pivot_cell)
                pivot_cell = sheet.cell(row=x, column=y)
                blank_count_h = 0
            else:
                blank_count_h += 1
                y += 1
                pivot_cell = sheet.cell(row=x, column=y)

        y = 1
        x += 1
        pivot_cell = sheet.cell(row=x, column=y)
        if(check_title(pivot_cell)):
            blank_count_h = 0
        elif(check_unused(pivot_cell)):
            print("blank v on cell ", x, y)
            blank_count_v += 1
        elif(check_coaching_notes(pivot_cell)):
            print("found a coaching notes cell!")
            blank_count_v = 0
            x += 4
        else:
            blank_count_v = 0


def read_workout(sheet, cell):
    print('Reading: ', cell.value)
    #while(cell.fill.start_color.index == 'FF000000')
    #print(cell.value)
    # start at provided cell
    # iterate through rows and columns of singular workouts
    # record data to list/dict
    # return list/dict

