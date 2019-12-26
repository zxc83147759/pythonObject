from django.contrib import admin
from .models import Sentence

# Register your models here.
class SentenceAdmin(admin.ModelAdmin):
    fields =['original_text','encoding_text']

admin.site.register(Sentence,SentenceAdmin)
