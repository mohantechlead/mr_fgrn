from django.urls import path
from .views import mr

urlpatterns = [
    path('mr_base', mr.mr_base, name='mr_base'),
]