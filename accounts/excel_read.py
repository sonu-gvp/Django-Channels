import xlrd

def excel(path):
	wb = xlrd.open_workbook(path)
	sheet = wb.sheet_by_index(0)
	for i in range(sheet.nrows):
		for j in range(sheet.ncols):
			result =  sheet.cell_value(i,j)
			print("function>>", result)
			return result
