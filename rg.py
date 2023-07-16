import openpyxl

# Create a new workbook and select the active sheet
workbook = openpyxl.Workbook()
sheet = workbook.active

# Add data to the sheet
data = [
    ['Name', 'Age', 'City'],
    ['John', 25, 'New York'],
    ['Alice', 30, 'London'],
    ['Bob', 35, 'Paris']
]

for row in data:
    sheet.append(row)

# Save the workbook
workbook.save('data.xlsx')
