from django.db import models

# Create your models here.():
class Test(models.Model):
	"""docstring for ClassName"""
	first_name = models.TextField(max_length=20)
	last_name = models.TextField(max_length=20)
	email = models.EmailField(max_length=254)
	mobile = models.TextField(max_length=15)
