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


class Dpsreport(models.Model):
	SHIFT_CHOICES = [
	('Day','Day'),
	('Night','Night'),
	('Over Night','Over Night'),
	]

	dia = models.CharField(max_length=35)
	operator_name = models.ForeignKey(Employees, on_delete=models.CASCADE)
	date = models.DateField(blank=True, null=True)
	shift = models.CharField(max_length=25, choices=SHIFT_CHOICES)
	party_name = models.ForeignKey(Vendor, on_delete=models.CASCADE)
	job_dc_no = models.ForeignKey(Production, on_delete=models.CASCADE)
	mr_mill_counts = models.CharField(max_length=35)
	mr_lot_no = models.CharField(max_length=35)
	mr_lycra_denier = models.CharField(max_length=35)
	mr_mill_plyester = models.CharField(max_length=35)
	prgm_dia = models.CharField(max_length=35)
	prgm_gsm = models.CharField(max_length=35)
	prgm_lopp_length = models.CharField(max_length=35)
	prgm_knitting_type = models.CharField(max_length=35)
	fabric_quality = models.CharField(max_length=35)
	co_ordinator = models.CharField(max_length=35)
	qc_instruction = models.CharField(max_length=35)
	roll_no = models.CharField(max_length=35)
	start_time = models.DateField(blank=True, null=True)
	end_time = models.DateField(blank=True, null=True)
	weight = models.CharField(max_length=35)
	machine_counting = models.CharField(max_length=35)
	holes = models.CharField(max_length=35)
	set_off = models.CharField(max_length=35)
	lycra_jump = models.CharField(max_length=35)
	lycra_cut = models.CharField(max_length=35)
	polyester_mis_cut = models.CharField(max_length=35)
	contamination = models.CharField(max_length=35)
	thickyarn = models.CharField(max_length=35)
	needle_line = models.CharField(max_length=35)
	oil_line = models.CharField(max_length=35)
	needel_br_t1 = models.CharField(max_length=35)
	needel_br_t2 = models.CharField(max_length=35)
	needel_br_t3 = models.CharField(max_length=35)
	needel_br_s = models.CharField(max_length=35)
	remarks = models.CharField(max_length=35)
	order_qty = models.CharField(max_length=35)
	completed_qty = models.CharField(max_length=35)
	balance_qty = models.CharField(max_length=35)
	created_at = models.DateTimeField(default=timezone.now)
	updated_at = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return f"{self.operator_name.name} - {self.party_name.name} - {self.job_dc_no} - {self.shift}"

