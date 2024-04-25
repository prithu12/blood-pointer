from django.urls import path
from .views import *

urlpatterns = [
    path('v1/', OpenDataView.as_view()),
]