from django.urls import path
from . import views

urlpatterns = [
    path('getAPI/', views.make_depositDB)
]
