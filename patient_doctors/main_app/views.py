from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Patient
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView
# Create your views here.
def home(request):
    return render(request, 'home.html')

def doctors(request):
    return render(request, 'doctors.html')

class PatientListView(View):
    def get(self, request):
        query_set = Patient.objects.all()
        context = {
            'patient_list': query_set
        }
        return render(request, 'patient/patient_list.html', context)

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

class PatientUpdate(UpdateView):
    model = Patient
    fields = ['age','symptoms','insurance','gender', 'address']
    


class PatientCreate(CreateView):
    model = Patient
    fields = '__all__'
    success_url = '/patients/'

def patient_delete(request,id):
    object = get_object_or_404(Patient, id = id)
    if request.method == "POST":
        #Comfirm delete so they don't delete it
        object.delete()
        return redirect('../../')
    context = {
        "patient_delete": object
    }
    return render(request, 'patient/patient_delete.html', context)
