from django.urls import path, include

urlpatterns = [
    path('patients/', include('api.urls.patient')),
    path('doctors/', include('api.urls.doctor')),
    path('nurses/', include('api.urls.nurse')),
    path('appointments/', include('api.urls.appointment')),
    path('consultations/', include('api.urls.consultation')),
    path('prescriptions/', include('api.urls.prescription')),
    path('labresults/', include('api.urls.labresult')),
    path('vitalsigns/', include('api.urls.vitalsign')),
]
