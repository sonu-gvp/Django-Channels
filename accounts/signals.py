from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.contrib.auth.models import User
from . models import Test
from . models1 import *
from . ronak import Hello
import openpyxl
from django.template.loader import render_to_string

# @receiver(post_delete,sender=User)
# @receiver(post_save, sender=User)
# def change_user(sender, instance, *args, **kwargs):
# 	users = User.objects.all()
# 	html_users = render_to_string("includes/users.html",{'users':users})
# 	channel_layer = get_channel_layer()
# 	async_to_sync(channel_layer.group_send)(
# 		"users",
# 		{
# 			"type":"user_update",
# 			"event":"New User",
# 			'html_users': html_users,
# 		}
# 	)


@receiver(post_delete,sender=Hello)
@receiver(post_save, sender=Hello)
def change_user(sender, instance, *args, **kwargs):
	hello = Hello.objects.all()
	hello_users = render_to_string("includes/hello.html",{'hello':hello})
	channel_layer = get_channel_layer()
	async_to_sync(channel_layer.group_send)(
		"hello",
		{
			"type":"user_update",
			"event":"New User",
			'html_hello': hello_users,
		}
	)

# @receiver(post_delete,sender=MyappRegistr)
# @receiver(post_save, sender=MyappRegistr)
# def change_user(sender, instance, *args, **kwargs):
# 	register = MyappRegistr.objects.all()
# 	html_register = render_to_string("includes/register.html",{'register':register})
# 	channel_layer = get_channel_layer()
# 	async_to_sync(channel_layer.group_send)(
# 		"users",
# 		{
# 			"type":"user_update",
# 			"event":"New User",
# 			'html_register': html_register,
# 		}
# 	)

# @receiver(post_delete,sender=Test)
# @receiver(post_save, sender=Test)
# def test_user(sender, instance, *args, **kwargs):
# 	tests = Test.objects.all()
# 	channel_layer = get_channel_layer()
# 	wb = openpyxl.load_workbook('/home/user/Downloads/Employee data.xlsx')
# 	# getting a particular sheet by name out of many sheets
# 	worksheet = wb["Employee data"]
# 	excel_data = list()
# 	for row in worksheet.iter_rows():
# 		row_data = list()
# 		for cell in row:
# 			row_data.append(str(cell.value))
# 		excel_data.append(row_data)
# 	html_excel = render_to_string("includes/excel.html",{"excel_data":excel_data})
# 	async_to_sync(channel_layer.group_send)(
# 		"tests",
# 		{
# 			"type":"user_update",
# 			"event":"New User",
# 			'html_excel' : html_excel,
# 		}
# 	)
# 	html_test = render_to_string("includes/test.html",{'tests':tests})
# 	async_to_sync(channel_layer.group_send)(
# 		"tests",
# 		{
# 			"type":"user_update",
# 			"event":"New User",
# 			'html_test': html_test,
# 		}
# 	)
