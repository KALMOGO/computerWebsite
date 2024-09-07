from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.
admin.site.register([App, Page, SliderInfo, userMessage, usefulLink, Testimony])
