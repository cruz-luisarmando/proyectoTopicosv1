from django.contrib import admin
from .models import Tutoriallac
from tinymce import TinyMCE
from django.db import models

class TutorialTinyLac(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget':TinyMCE()}
    }

# Register your models here.

admin.site.register(Tutoriallac, TutorialTinyLac)
