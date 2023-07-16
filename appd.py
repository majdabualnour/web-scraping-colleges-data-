import openpyxl
import vff
# Load the Excel file
workbook = openpyxl.load_workbook('thefile.xlsx')

# Select the specific worksheet
worksheet = workbook['Sheet1']  # Replace 'Sheet1' with the name of your worksheet

# Specify the column letter
target_column = 'D'  # Replace with the desired column letter

# Retrieve data from the specific column
column_data = []

for cell in worksheet[target_column]:
    if cell.value:
        column_data.append(cell.value)
nf  =6

# Print the retrieved data
for cell_value in column_data:
    nf +=1
    if nf >2:
        valu1 , valu2,valu3,valu4,valu5,valu6,valu7,valu8,valu9,valu10,valu11,valu12  =  vff.getalluwnat(cell_value)


        worksheet[f'B{nf}'] = 'USA'
        worksheet[f'C{nf}'] = valu1
        worksheet[f'E{nf}'] = valu2
        worksheet[f'H{nf}'] = 'Not specified'
        worksheet[f'J{nf}'] = valu3
        worksheet[f'K{nf}'] = valu4
        worksheet[f'L{nf}'] = valu5
        worksheet[f'M{nf}'] = valu6
        worksheet[f'N{nf}'] = valu7
        worksheet[f'O{nf}'] = valu8
        worksheet[f'Q{nf}'] = 'Not specified'
        worksheet[f'R{nf}'] = valu9
        worksheet[f'S{nf}'] = valu10
        worksheet[f'T{nf}'] = valu11
        worksheet[f'U{nf}'] = valu12
        worksheet[f'V{nf}'] = valu12
        worksheet[f'W{nf}'] = valu12
        worksheet[f'X{nf}'] = 'N/A'
        worksheet[f'Y{nf}'] = 'N/A'
        worksheet[f'Z{nf}'] = 'YES'
        
