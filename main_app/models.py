from django.db import models
from django.urls import reverse
# Create your models here.

class Doctor (models.Model):
    name = models. CharField(max_length = 150)
    age = models.IntegerField()
    gender = models.CharField(max_length = 50)
    specialization = models.CharField(max_length = 200, null = True)
    office_location = models.CharField(max_length = 500)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"doctors/{self.id}"

class Patient (models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    symptoms = models.TextField()
    insurance = models.CharField(max_length = 250)
    gender = models.CharField(max_length = 50)
    address = models.TextField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f"/patients/{self.id}"
    # def get_absolute_url(self):
    #     return reverse('detail', kwargs={'id': self.id})

class Medication (models.Model):
    name = models.CharField(max_length=250)
    amount = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f"/medications/{self.id}"

class PatientDoctor(models.Model):
    patient = models.ForeignKey(Patient, on_delete= models.CASCADE, default = 1, related_name='patients')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, default = 1, related_name='doctors')
    medicine = models.ForeignKey(Medication, on_delete= models.CASCADE, default = 1, related_name='medicine')

# class MedicationDoctor (models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, default = 1, related_name='doctors')
#     medicine = models.ForeignKey(Medications, on_delete= models.CASCADE, default = 1, related_name='medicine')


# class MedicationPatient (models.Model):
#     patient = models.ForeignKey(Patient, on_delete= models.CASCADE, default = 1, related_name='patients')
#     medicine = models.ForeignKey(Medications, on_delete= models.CASCADE, default = 1, related_name='medicine')



