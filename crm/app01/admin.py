from django.contrib import admin

# Register your models here.
from app01 import models
class CourseRecordAdmin(admin.ModelAdmin):
    list_display = ['day_num', 'date', 'course_title', 'homework_title']
    list_editable = ['course_title', 'homework_title']
admin.site.register(models.Userinfo)
admin.site.register(models.Customer)
admin.site.register(models.Campuses)
admin.site.register(models.ClassList)
admin.site.register(models.ConsultRecord)
admin.site.register(models.Enrollment)
admin.site.register(models.CourseRecord,CourseRecordAdmin)
admin.site.register(models.StudyRecord)
