from django.contrib import admin
from .models import Production, Dpsreport
from .models import Employees
from vendors.models import Vendor, Lead
from .models import Machine

# Register your models here.
admin.site.register(Employees)
admin.site.register(Vendor)
admin.site.register(Machine)
admin.site.register(Production)
admin.site.register(Lead)
admin.site.register(Dpsreport)
