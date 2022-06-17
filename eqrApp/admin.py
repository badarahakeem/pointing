from django.contrib import admin
from eqrApp import models

# Register your models here.

@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display =  ('id', 'employee_code', 'first_name', 'last_name')



admin.site.register(models.Pointing)
# admin.site.register(models.Employee)

