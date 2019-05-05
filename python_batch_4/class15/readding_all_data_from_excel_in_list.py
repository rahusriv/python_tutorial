import xlrd
import xlwt
import datetime
from xlwt import Workbook

NO_OF_COLUMNS = 6
NO_OF_ROWS = 38

# Give the location of the file
loc = ("/home/rahul/Desktop/FormsToBeDeleted.xlsx")

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

# For row 0 and column 0
for i in range(0, NO_OF_ROWS):
    row = []
    for j in range(0, NO_OF_COLUMNS):
        #print(type(sheet.cell_value(i,j)))
        row.append(sheet.cell_value(i,j))
    print(row)

data = sheet.cell_value(0,3)
print(type(data))
print(datetime.datetime.fromtimestamp(data))
#data = sheet.cell_value(0, 0)

#print(data)

loc = ("/home/rahul/Desktop/FormsToBeDeleted.xlsx")

# To open Workbook
wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')
wb.save('xlwt example.xls')



