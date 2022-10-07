from django.contrib import admin
from .models import Buyplan, Plan

# Register your models here.
@admin.register(Plan)
class SliderModelAdmin(admin.ModelAdmin):
    list_display =['id','amount','sms','data','roaming','subscription']

@admin.register(Buyplan)
class SliderModelAdmin(admin.ModelAdmin):
    list_display =['id','amount','sms','data','roaming','subscription']