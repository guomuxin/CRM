from django.contrib import admin

# Register your models here.
from app01 import models
admin.site.register(models.Userinfo)
admin.site.register(models.Customer)
admin.site.register(models.Campuses)
admin.site.register(models.ClassList)
admin.site.register(models.ConsultRecord)
admin.site.register(models.Enrollment)
