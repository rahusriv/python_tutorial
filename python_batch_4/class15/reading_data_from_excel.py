import xlrd

NO_OF_COLUMNS = 6
NO_OF_ROWS = 38

# Give the location of the file
loc = ("/home/rahul/Desktop/FormsToBeDeleted.xlsx")

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

# For row 0 and column 0
data = sheet.cell_value(0, 0)

print(data)


