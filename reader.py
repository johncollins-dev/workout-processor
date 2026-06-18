'''
reader.py
'''
from openpyxl import load_workbook

def read(filename):
    wb = load_workbook(filename)
    ws = wb.active
    print(wb.sheetnames)

    # iterate through sheets until 'Week 1' is found
    # set 'Week 1' as active
    # Run builder, create new block with layer value 1 and title 'Week 1'
    # iterate through columns until cell with black bg, white fg, and bold
    # text is found
    #
