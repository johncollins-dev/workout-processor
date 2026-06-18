'''
reader.py
'''
from openpyxl import load_workbook

def find_title_cell(sheet):
    # iterate through columns until cell with black bg, white fg, and bold
    # text is found

def read(filename):
    wb = load_workbook(filename)
    ws = wb.active
    #print(wb.sheetnames)

    # iterate through sheets until 'Week 1' is found
    for sheet in wb.worksheets:
        if (sheet.title == 'Week 1'):
            print('found week 1:')
            sheet = wb.active
            find_title_cell(sheet)

    # set 'Week 1' as active
    # Run builder, create new block with layer value 1 and title 'Week 1'
    #
