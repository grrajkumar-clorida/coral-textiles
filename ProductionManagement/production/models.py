from django.db import models
from employee.models import Employees
from machines.models import Machine
from vendors.models import Vendor
from django.utils import timezone

class Production(models.Model):
	name = models.CharField(max_length=50)
	shift = models.CharField(max_length=20)
	employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
	vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
	machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
	from_date = models.DateField()
	to_date = models.DateField()
	report = models.TextField()
	image = models.ImageField(upload_to='production_images/')
	created_at = models.DateTimeField(default=timezone.now)
	updated_at = models.DateTimeField(blank=True, null=True)

	# Update fabric to be a dropdown
	FABRIC_CHOICES = [
	('40 S + 20 D', '40 S + 20 D'),
	('34 S + 20 D', '34 S + 20 D'),
	('30 S + 40 D', '30 S + 40 D'),
	('HELPER', 'HELPER'),
	('SERVICE', 'SERVICE'),
	]
	fabric = models.CharField(max_length=50, choices=FABRIC_CHOICES)

	SHIFT_CHOICES = [
	('Day','Day'),
	('Night','Night'),
	('Over Night','Over Night'),
	]
	shift = models.CharField(max_length=25, choices=SHIFT_CHOICES)

	STATUS_CHOICES = [
	('Pipe Line', 'Pipe Line'),
	('Open', 'Open'),
	('In Progress', 'In Progress'),
  	('Completed', 'Completed'),
   	('Done', 'Done'),
   	('Due', 'Due'),
    ]
	status = models.CharField(max_length=25, choices=STATUS_CHOICES)

	def __str__(self):
		return self.name
		#return f"{self.vendor.name} - {self.machine.name} - {self.fabric} - {self.status}"


