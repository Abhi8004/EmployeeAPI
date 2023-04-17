from django.contrib import admin
from api.models import Company,Employee

# Register your models here

class CompanyAdmin(admin.ModelAdmin):
    list_display=('company_name','address')
    search_fields=('company_name',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','email','company')
    list_filter=('company',)
    search_fields=('name',)

admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)


