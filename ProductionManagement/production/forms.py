from django import forms
from .models import Production, Employees, Vendor, Machine

class ProductionForm(forms.ModelForm):
    employee   = forms.ModelChoiceField(queryset=Employees.objects.all(), empty_label="Select Employee")
    vendor     = forms.ModelChoiceField(queryset=Vendor.objects.all(), empty_label="Select Vendor")
    machine    = forms.ModelChoiceField(queryset=Machine.objects.all(), empty_label="Select System")
    shift      = forms.ChoiceField(choices=[('', 'Select Shift')] + Production.SHIFT_CHOICES)  # Explicitly use choices
    status     = forms.ChoiceField(choices=[('', 'Select Status')] + Production.STATUS_CHOICES, required=True )
    fabric     = forms.ChoiceField(choices=[('', 'Select fabric')] + Production.FABRIC_CHOICES, required=True )
    name       = forms.ModelChoiceField(
        queryset=Production.objects.all(),  # Fetch all Production instances
        empty_label="Select Name",  # Customize the placeholder
        to_field_name="name",  # Use the name field for the dropdown display
    )
    
    class Meta:
        model = Production
        fields = ['shift', 'employee', 'vendor', 'name', 'machine', 'fabric', 'image', 'from_date', 'to_date', 'status']
        widgets = {
            'from_date': forms.DateInput(attrs={'type': 'date'}),
            'to_date': forms.DateInput(attrs={'type': 'date'}),
        }
