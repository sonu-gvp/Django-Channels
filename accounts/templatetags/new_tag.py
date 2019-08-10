from django import template
from accounts.views import excel_data

register = template.Library()

@register.filter()
def get_result_tag(excel_data):
		return excel_data
