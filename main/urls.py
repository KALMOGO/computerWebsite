from django.urls import  path

from . import views

urlpatterns = [
    path("", view=views.home, name="index"),
    path("contact", view=views.contact, name="contact"),
    path("about", view=views.about, name="about"),
    path("privacies", view=views.privacy, name="privacies"), 
    path("recommendation", view=views.recommendation, name="recommendation"),
    path("order/zoodoAI", view=views.recommendationForm, name="recommendationForm"),
    path("withouai_step2", view=views.withouai_validateStep2, name='withouai_step2'),
    path("recommendations", view=views.withai_recommendation, name="withai_submit"),
    path("detail/<str:id>/<str:time>", view=views.detail, name="detail"),
    path("success/order", view=views.successPage, name="success-order"),
    path("error/page", view=views.errorPage, name="error-page"),
    path("commander", view=views.processOrderPage, name="process-order"),
    path("order/simple", view=views.recommendationFormWithoutAI, name="order-without-ai"),
]