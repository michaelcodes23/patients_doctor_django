from django.contrib import admin
from .models import Medication, Patient, Doctor, PatientDoctor
# Register your models here.

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(PatientDoctor)
admin.site.register(Medication)