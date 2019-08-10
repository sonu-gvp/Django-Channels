from django.shortcuts import render
from django.contrib.auth.models import User
import openpyxl
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth import models
from . ronak import *

def new_user(request):
	users = Hello.objects.all()
	return render(request, 'new_user.html',{'hello':users})

def excel_data(request):
	wb = openpyxl.load_workbook('/home/user/Downloads/Employee data.xlsx')
	# getting a particular sheet by name out of many sheets
	worksheet = wb["Employee data"]
	excel_data = list()
	for row in worksheet.iter_rows():
		row_data = list()
		for cell in row:
			row_data.append(str(cell.value))
		excel_data.append(row_data)
	return render(request, 'includes/excel.html', {"excel_data":excel_data})

def insert(request):
	obj = Hello(id=13,first_name="hello1", last_name="hello1", email="hello1@gmail.com",
		mobile="9725562271")
	obj.save()
	return HttpResponse("success")