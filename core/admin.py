from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Hospital)
admin.site.register(User)
admin.site.register(Patient)
admin.site.register(MedicalHistory)
admin.site.register(Diagnostic)
admin.site.register(Equipment)
admin.site.register(Referral)