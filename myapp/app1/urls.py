from django.urls import path
from . import views

urlpatterns = [
    path('app/', views.app, name='app'),
    path('app2/', views.app2, name='app2')
]
