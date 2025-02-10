from django.urls import path # type: ignore
from all_ems.views import *

urlpatterns=[
    path("",home,name="home")
]
