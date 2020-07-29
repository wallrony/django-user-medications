from django.contrib import admin
from user_medications.core import models

# Register your models here.

class MedicationAdmin(admin.ModelAdmin):
  fields = ('id', 'nome', 'validade', 'user_id')
  search_fields = ['id', 'nome', 'validade']

admin.site.register(models.Medication, MedicationAdmin)