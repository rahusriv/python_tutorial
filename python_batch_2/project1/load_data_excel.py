
# Program to extract number of
# columns in Python
import xlrd

loc = ("data.xlsx")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

# For row 0 and column 0
print(sheet.cell_value(0, 0))
print(sheet.row_values(1))
# Extracting number of columns
print(sheet.ncols)

for i in range(0,5):
    print(sheet.row_values(i))
