from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="dogs.all"),
    path("<int:id>/",views.show,name="dog.show")
]