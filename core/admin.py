from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model=User


# Register your models here.
admin.site.register(Hospital)
admin.site.register(Patient)
admin.site.register(MedicalHistory)
admin.site.register(Diagnostic)
admin.site.register(Equipment)
admin.site.register(Referral)
admin.site.register(User, CustomUserAdmin)