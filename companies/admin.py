from django.contrib import admin
from .models import ActivityCatalog, JobCatalog, DepartmentsCatalog, CompanyUser, CompanyEmployees, BranchCompany

admin.site.register(ActivityCatalog)
admin.site.register(JobCatalog)
admin.site.register(DepartmentsCatalog)
admin.site.register(CompanyUser)
admin.site.register(CompanyEmployees)
admin.site.register(BranchCompany)
