# """crm URL Configuration
#
# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/1.11/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.conf.urls import url, include
#     2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
# """
# from django.conf.urls import url,include
# from django.contrib import admin
#
# urlpatterns = [
#     url(r'^app01/',include('app01.urls',namespace='app01'))
#
# ]
from django.conf.urls import url,include
from django.contrib import admin
from app01 import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.Login.as_view(),name='login'),
    url(r'^register/', views.Register.as_view(),name='register'),
    url(r'^home/', views.Home.as_view(),name='home'),
    url(r'^customer_info/', views.Customer_Info.as_view(),name='customer_info'),
    url(r'^private_customer/', views.Customer_Info.as_view(),name='private_customer'),
    url(r'^add_customer/', views.Add_Edit_Customer.as_view(),name='add_customer'),
    url(r'^edit_customer/(\d+)', views.Add_Edit_Customer.as_view(),name='edit_customer'),
    url(r'^del_customer/(\d+)', views.Del_Customer.as_view(),name='del_customer'),
    url(r'^logout/', views.Logout.as_view(),name='logout'),
    url(r'^consult_record/(\d+)', views.Consult_Record.as_view(), name='consult_record_one'),
    url(r'^consult_record/', views.Consult_Record.as_view(),name='consult_record'),
    url(r'^consult_record_edit/(\d+)', views.Consult_Record_Edit.as_view(),name='consult_record_edit'),
    url(r'^consult_record_add/', views.Consult_Record_Edit.as_view(),name='consult_record_add'),
    url(r'^consult_record_del/(\d+)', views.Consult_Record_Del.as_view(),name='consult_record_del'),
    url(r'^enrollment/', views.EnrollmentInfo.as_view(),name='enrollment_info'),
    url(r'^enrollment_add/', views.EnrollmentAddEdit.as_view(),name='enrollment_add'),
    url(r'^enrollment_edit/(\d+)', views.EnrollmentAddEdit.as_view(),name='enrollment_edit'),
    url(r'^enrollment_del/(\d+)', views.EnrollmentDel.as_view(),name='enrollment_del'),
    url(r'^CourseRecord/info/', views.CourseRecordInfo.as_view(),name='coure_record_info'),
    url(r'^CourseRecord/add/', views.CourseRecordAddEdit.as_view(),name='coure_record_add'),
    url(r'^CourseRecord/edit/(\d+)', views.CourseRecordAddEdit.as_view(),name='coure_record_edit'),
    url(r'^CourseRecord/del/(\d+)', views.CourseRecordDel.as_view(),name='coure_record_del'),
    url(r'^studyRecord/info/', views.StudyRecordInfo.as_view(), name='studyRecord_info'),
    url(r'^rbac/', include('rbac.urls', namespace='rbac'))

]