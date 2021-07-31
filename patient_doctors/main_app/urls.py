
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('patients/', views.PatientListView.as_view(), name = 'patients'),
    path('patients/<int:id>/', views.patient_detail, name = 'patient-detail'),
    path('patients/create/', views.PatientCreate.as_view(), name = 'patient-create'),
    path('patients/<int:id>/update/', views.PatientUpdate.as_view(), name = 'patient-update'),
    path('patients/<int:id>/delete/', views.patient_delete, name = 'patient-delete'),
    path('doctors/', views.doctors, name = 'doctors'),
]