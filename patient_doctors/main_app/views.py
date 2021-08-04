from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Medication, Patient, Doctor
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView
# Create your views here.
def home(request):
    return render(request, 'home.html')
# Patient Views

class DoctorListView(View):
    def get(self, request):
        query_set = Doctor.objects.all()
        context_doctor = {
            'doctors': query_set
        }
        return render(request, 'doctor/doctor_list.html', context_doctor)


class PatientListView(View):
    def get(self, request):
        query_set = Patient.objects.all()
        context = {
            'patient_list': query_set
        }
        return render(request, 'patient/patient_list.html', context)

class MedicineListView(View):
    def get(sef, request):
        query_set= Medication.objects.all()
        context = {
            'medicine_list': query_set
        }
        return render(request, 'medicine/medicine_list.html', context)

# function view
# def patient_list(request, id):
#     query_set = Patient.objects.all()
#     context = {
#         'patient_list': query_set
#     }
#     return render(request, 'patient/patient_list.html', context)

def patient_detail(request, id):
    object = Patient.objects.get(id = id)
    context = {
        'patient_detail': object
    }
    return render(request, 'patient/patient_detail.html', context)

def doctor_detail(request, id):
    object = Doctor.objects.get(id = id)
    context = {
        'doctor_detail': object
    }
    return render(request, 'doctor/doctor_detail.html', context)

def medicine_detail(request, id):
    object = Medication.objects.get(id = id)
    context = {
        'medicine_detail': object
    }
    return render (request, 'medicine/medicine_detail.html', context)

class PatientUpdate(UpdateView):
    model = Patient
    fields = ['age','symptoms','insurance','gender', 'address']

class DoctorUpdate(UpdateView):
    model = Doctor
    fields = ['name', 'age', 'specialization', 'office_location']
    template_name = 'doctor/doctor_create.html'

class MedicineUpdate(UpdateView):
    model = Medication
    fields = ['amount','description']
    template_name = 'medicine/medicine_create.html'

class PatientCreate(CreateView):
    model = Patient
    fields = '__all__'
    template_name = 'patient/patient_create.html'
    success_url = '/patients/'

class DoctorCreate(CreateView):
    model = Doctor
    fields = '__all__'
    template_name = 'doctor/doctor_create.html'
    success_url = '/doctors/'

class MedicineCreate(CreateView):
    model = Medication
    fields = '__all__'
    template_name = 'medicine/medicine_create.html'
    success_url = '/medicines/'
# def patient_delete(request,id):
#     object = get_object_or_404(Patient, id = id)
#     if request.method == "POST":
#         #Comfirm delete so they don't delete it
#         object.delete()
#         return redirect('../../')
#     context = {
#         "patient_delete": object
#     }
#     return render(request, 'patient/patient_delete.html', context)

class PatientDelete(DeleteView):
    model= Patient
    template_name = 'patient/patient_delete.html'
    success_url = '/patients/'

class DoctorDelete(DeleteView):
    model= Doctor
    template_name = 'doctor/doctor_delete.html'
    success_url = '/doctors/'

class MedicineDelete(DeleteView):
    model = Medication
    template_name = 'medicine/medicine_delete.html'
    success_url = '/medicines/'