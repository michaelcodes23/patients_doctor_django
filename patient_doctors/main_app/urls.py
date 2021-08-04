
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('patients/', views.PatientListView.as_view(), name = 'patients'),
    path('patients/<int:id>/', views.patient_detail, name = 'patient-detail'),
    path('doctors/', views.DoctorListView.as_view(), name = 'doctors'),
    path('doctors/<int:id>', views.doctor_detail, name = 'doctor-detail'),
    path('medicines/', views.MedicineListView.as_view(), name = 'medicine'),
    path('medicines/<int:id>', views.medicine_detail, name = 'medicine-detail'),
    path('patients/create/', views.PatientCreate.as_view(), name = 'patient-create'),
    path('doctors/create/', views.DoctorCreate.as_view(), name = 'doctor-create'),
    path('medicines/create/', views.MedicineCreate.as_view(), name = 'medicine-create'),
    path('patients/<int:pk>/update/', views.PatientUpdate.as_view(), name = 'patient-update'),
    path('doctors/<int:pk>/update/', views.DoctorUpdate.as_view(), name = 'doctor-update'),
    path('medicines/<int:pk>/update', views.MedicineUpdate.as_view(), name = 'medicine-update'),
    path('patients/<int:pk>/delete/',views.PatientDelete.as_view(),name='patient-delete'),
    path('doctors/<int:pk>/delete/',views.DoctorDelete.as_view(), name = 'doctor-delete'),
    path('medicines/<int:pk>/delete/', views.MedicineDelete.as_view(), name = 'medicine-delete'),
]