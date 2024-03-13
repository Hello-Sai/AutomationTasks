from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('verify/<token>',views.verify,name="verify")
]