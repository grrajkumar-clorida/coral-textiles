from django.contrib import admin
from .models import Production
from .models import Employees
from .models import Vendor
from .models import Machine

# Register your models here.
admin.site.register(Employees)
admin.site.register(Vendor)
admin.site.register(Machine)
admin.site.register(Production)

