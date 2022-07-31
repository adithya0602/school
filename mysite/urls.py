from django.contrib import admin
from django.urls import path
from mysite import views
# url creations for all the web pages
urlpatterns = [
    path("",views.index,name="home"),
    path("tregister",views.tregister,name="tregister"),
    path("sregister",views.sregister,name="sregister"),
    path("slogin",views.slogin,name="slogin"),
    path("tlogin",views.tlogin,name="tlogin"),
    path("sprofile",views.sprofile,name="sprofile"),
    path("tprofile",views.tprofile,name="tprofile"),
]