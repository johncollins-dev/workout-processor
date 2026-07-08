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
    
    # are these even needed or can I just move the pivot_cell inline like
    # pivot_cell=sheet.cell(row=x+1, column=1)
    x = 1
    y = 1
    pivot_cell = sheet.cell(row=x, column=y)

    blank_count_h = 0
    blank_count_v = 0

    # go row by row of workout sections
    #while( black cell count is less than 2):
    while(blank_count_v < 2):
        #print("iterating v")
        #breakpoint()
        # scan sheets horizontally until after last sheet is read
        #while(black_cell count is less than 2):
        while(blank_count_h < 2):
            #print("iterating h")
            # check that the cell is a title cell
            if(check_title(pivot_cell)):
                # yes - read workout, put the pivot at y += workout_width, blank cell count 0
                #sheet_data.extend(read_workout(sheet, pivot_cell))
                read_workout(sheet, pivot_cell)
                y += get_workout_width(sheet, pivot_cell)
                pivot_cell = sheet.cell(row=x, column=y)
                blank_count_h = 0
            # else
            else:
                # increase blank cell count by one
                blank_count_h += 1
                # put the pivot at y+= 1
                y += 1
                pivot_cell = sheet.cell(row=x, column=y)

        # put the pivot at y=1
        y = 1
        # put the pivot at x+1
        x += 1
        pivot_cell = sheet.cell(row=x, column=y)
        #if(x == 24): print("cell value at x 24: ", pivot_cell.value)
        #if(x == 25): print("cell value at x 25: ", pivot_cell.value)
        #print("x: ", x)
        # check if pivot is title cell
        if(check_title(pivot_cell)):
            # yes - blank_cell count horizontal is 0, 
            blank_count_h = 0
        # else, check if cell at pivot is unused
        elif(check_unused(pivot_cell)):
            # yes - blank_cell count vertical += 1
            print("blank v on cell ", x, y)
            blank_count_v += 1
        #else, x+=1
        elif(check_coaching_notes(pivot_cell)):
            print("found a coaching notes cell!")
            blank_count_v = 0
            x += 4
        #else:
            #x += 1


def read_workout(sheet, cell):
    print('Hi!')
    #while(cell.fill.start_color.index == 'FF000000')
    #print(cell.value)
    # start at provided cell
    # iterate through rows and columns of singular workouts
    # record data to list/dict
    # return list/dict

