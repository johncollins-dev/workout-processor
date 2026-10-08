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

def check_title(cell):
    if cell.value is not None:
        return (
            cell.value.startswith('Day')
            and cell.font.bold
            and cell.fill.start_color.index == 'FF000000'
        )

    return False


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
    wb.active = 3
    sheet = wb.active

    #temporary measure for testing read_sheet:
    print('reading sheet ', sheet.title)
    read_sheet(sheet)
    #for sheet in wb.worksheets:
    #    if(sheet.title.startswith('Week')):
    #       read_sheet(sheet)

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
    while(not check_coaching_notes(sheet.cell(row=r,column=c))):
        r += 1
        height += 1

    height += 4
    return height

def read_sheet(sheet):
    sheet_data = []
    
    x = 1
    y = 1
    pivot_cell = sheet.cell(row=x, column=y)

    blank_count_h = 0
    blank_count_v = 0
    
    workout_width = get_workout_width(sheet, pivot_cell)
    workout_height = get_workout_height(sheet, pivot_cell)

    # scan workout blocks vertically
    while(blank_count_v < 5):
        # scan workout blocks horizontally
        while(blank_count_h < 2):
            blank_count_v = 0
            if(check_title(pivot_cell)):
                #sheet_data.extend(read_workout(sheet, pivot_cell))
                read_workout(sheet, pivot_cell)
                y += workout_width
                pivot_cell = sheet.cell(row=x, column=y)
                blank_count_h = 0
            else:
                blank_count_h += 1
                y += 1
                pivot_cell = sheet.cell(row=x, column=y)

        y = 1
        x += workout_height
        pivot_cell = sheet.cell(row=x, column=y)
        while(not check_title(pivot_cell) and blank_count_v < 5):
            x += 1
            pivot_cell = sheet.cell(row=x, column=y)
            if(check_unused(pivot_cell)):
                blank_count_v += 1

        blank_count_h = 0

def read_workout(sheet, cell):
    print('Reading: ', cell.value)
    workout_data = []
    # start at provided cell
    c = cell.column
    r = cell.row
    pivot_cell = sheet.cell(row=r, column=c)
    width = get_workout_width(sheet, pivot_cell)
    height = get_workout_height(sheet, pivot_cell)
    for row in range(1, r+height-1):
        line = {}
        for col in range(1, c+width-1):
            pivot_cell = sheet.cell(row=row, column=col)
            if(pivot_cell.value == 'None'):
                line[col] = ''
            else:
                line[pivot_cell.column] = pivot_cell.value
            
        workout_data.extend(line)
        print(line)
        line.clear



    '''
    # iterate through rows and columns of singular workouts
    for row in sheet.iter_rows(min_row=r, max_col=c+width-1, max_row=r+height-1):
        # record data to list/dict
        line = {}
        for cell in row:
            if(cell.value == None):
                line[
            line[] = cell.value
        workout_data.extend(line)
        line.clear
    '''
    # delete empty rows
    # return list/dict

