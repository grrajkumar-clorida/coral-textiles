from django import forms
from .models import Lead

class ContactUsForm(forms.ModelForm):
	class Meta:
		model = Lead
		fields = ['name', 'email', 'phone', 'info',]
		widgets = {
			'message' : forms.Textarea(attrs={'rows': 4}),
		}
