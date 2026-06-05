from django.urls import path

from . import views


app_name = 'clinicians'

urlpatterns = [
    path('biodata/', views.biodata, name='biodata'),
    # path('request/verification/', views.request_verification, name='request_verification'),
    path('verification/', views.verification, name='verification'),
    path('verification/review/', views.verification_review, name='verification_review'),
    path('dashboard/', views.dashboard, name='dashboard'),
]



