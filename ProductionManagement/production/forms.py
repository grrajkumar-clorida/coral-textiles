from django import forms
from .models import Production, Employees, Vendor, Machine, Dpsreport

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


class DailyProductionReportForm(forms.ModelForm):
    operator_name   = forms.ModelChoiceField(queryset=Employees.objects.all(), empty_label="Select Operator")
    party_name     = forms.ModelChoiceField(queryset=Vendor.objects.all(), empty_label="Select Part Name")
#    machine    = forms.ModelChoiceField(queryset=Machine.objects.all(), empty_label="Select System")
    shift      = forms.ChoiceField(choices=[('', 'Select Shift')] + Production.SHIFT_CHOICES)  # Explicitly use choices
#    fabric     = forms.ChoiceField(choices=[('', 'Select fabric')] + Production.FABRIC_CHOICES, required=True )

    class Meta:
        model = Dpsreport
        fields = ['dia', 'operator_name', 'date', 'shift', 'party_name', 'job_dc_no', 'mr_mill_counts', 'mr_lot_no', 'mr_lycra_denier', 'mr_mill_plyester', 'prgm_dia', 'prgm_gsm', 'prgm_lopp_length', 'prgm_knitting_type', 'fabric_quality', 'co_ordinator', 'qc_instruction', 'roll_no', 'start_time', 'end_time', 'weight', 'machine_counting', 'holes', 'set_off', 'lycra_jump', 'lycra_cut', 'polyester_mis_cut', 'contamination', 'thickyarn', 'needle_line', 'oil_line', 'needel_br_t1', 'needel_br_t2', 'needel_br_t3', 'needel_br_s', 'remarks', 'order_qty', 'completed_qty', 'balance_qty']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.DateInput(attrs={'type': 'date'}),
            'end_time': forms.DateInput(attrs={'type': 'date'}),
        }
