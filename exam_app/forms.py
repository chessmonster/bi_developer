from django import forms
from .models import test_table


class test_tableForm(forms.ModelForm):
		class Meta:
				model = test_table
				fields = ['name', ]

				
