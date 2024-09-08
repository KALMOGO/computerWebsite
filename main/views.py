from django.shortcuts import render
from .models import *
from article import models

def home(request) :
    context = {
        "page_title":"index.ph"
    }
    
    return render(request,"home.html", context)


def recommendation(request) :
    context = {
        "page_title":"recommandation.ph"
    }
    
    return render(request,"recommendation.html", context)



def contact(request) :
    context = {
        "page_title":"contact.ph"
    }
    
    return render(request,"contact.html", context)



def privacy(request) :
    context = {
        "page_title":"privacies.ph"
    }
    
    return render(request,"privacy.html", context)




def about(request) :
    context = {
        "page_title":"infos.ph"
    }
    
    return render(request,"about.html", context)

