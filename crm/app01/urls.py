from django.conf.urls import url
from django.contrib import admin
from app01 import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.Login.as_view(),name='login'),
    url(r'^register/', views.Register.as_view(),name='register'),
    url(r'^customer/', views.Customer.as_view(),name='customer'),

]