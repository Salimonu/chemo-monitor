from django.urls import path

from . import views

app_name = 'patients'

urlpatterns = [
    path('biodata/', views.biodata, name='biodata' ),
    path('dashboard/', views.dashboard, name='dashboard' ),
]
