from django.urls import  path

from . import views

urlpatterns = [
    path("", view=views.home, name="index"),
    path("contact", view=views.contact, name="contact"),
    path("about", view=views.about, name="about"),
    path("privacies", view=views.privacy, name="privacies"),
    path("recommendation", view=views.recommendation, name="recommendation"),
]