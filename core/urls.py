from django.urls import path, include

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index' ),
    path('signup/', views.signup, name='signup' ),
    path('user/', include('django.contrib.auth.urls')),
]
