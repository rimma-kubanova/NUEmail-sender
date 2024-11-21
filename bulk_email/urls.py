from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_csv_and_schedule, name='upload_csv_and_schedule'),
]
