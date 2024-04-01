from django.urls import path
from srh.views import *
app_name='srh_fan'

urlpatterns=[
    path('Captain/',Captain,name='cummins'),
]