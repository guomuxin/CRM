from django import forms
import re
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from app01 import models
# from multiselectfield import *
# from multiselectfield import  MultiSelectField
# from multiselectfield import  forms as ff



def mobile_validate(value):
    mobile_re = re.compile(r'^(13[0-9)|15[0-9]|17[678]|18[0-9])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError("手机号格式错误")


class MyForm(forms.Form):
    username = forms.CharField(
        min_length=2,
        widget=forms.TextInput(attrs={'class':'username','placeholder':'您的用户名'}),
        error_messages={
            'min_length':"用户名长度太短",
            'required':'用户名不能为空'
        }
    )

    password = forms.CharField(
        min_length=6,
        widget=forms.PasswordInput(attrs={'class':'password','placeholder':'输入密码'}),
        error_messages={
            'min_length':'密码不能低于6位',
            'required':'密码不能为空'
        }
    )

    confirm_password = forms.CharField(
        min_length=6,
        widget=forms.PasswordInput(attrs={'class':'confirm_password','placeholder':'再次输入密码'}),
        error_messages={
            'required': '确认密码不能为空'

        }

    )

    phone_number = forms.CharField(
        max_length=11,
        min_length=11,
        widget=forms.TextInput(attrs={'class':'phone_number','placeholder':'输入手机号'}),
        validators=[mobile_validate,],
        error_messages={
            'max_length':"请输入正确的手机号格式",
            'min_length':"请输入正确的手机号格式",
            'required': '电话不能为空'

        }
    )

    email = forms.CharField(
        widget=forms.TextInput(attrs={'class':'email','placeholder':'输入邮箱地址'}),
        error_messages={
            'required': '邮箱不能为空'

        }
    )

    def clean_email(self):
        value = self.cleaned_data.get('email')
        email_re = re.compile(r'.*@163.*')
        if email_re.match(value):
            return value
        else:
            raise ValidationError("请使用163邮箱")

    def clean(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password == confirm_password:
            return self.cleaned_data
        else:
            self.add_error('confirm_password',"两次密码输入不一致")

class CustomerForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        exclude = ['delete_status']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for i in self.fields.values():
            if i.label == "咨询课程":
                continue
            i.widget.attrs.update({'class':'form-control'})


class ConsultRecordForm(forms.ModelForm):
    class Meta:
        model = models.ConsultRecord

        exclude = ['delete_status']
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields.values():
            i.widget.attrs.update({'class': 'form-control'})
            if i.label == "所咨询客户":
                i.queryset=models.Customer.objects.filter(consultant__username=request.session.get("username"))
            if i.label == "跟进人":
                data = models.Userinfo.objects.filter(username=request.session.get("username"))
                i.choices = [(j.id, j.username) for j in data]


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = models.Enrollment
        exclude = ['delete_status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields.values():
            if i.label == "审批通过":
                continue
            i.widget.attrs.update({'class':'form-control'})



class CourseRecordForm(forms.ModelForm):
    class Meta:
        model = models.CourseRecord
        exclude = ['scoring_point','has_homework']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields.values():
            i.widget.attrs.update({'class':'form-control'})


class StudyRecordForm(forms.ModelForm):
    class Meta:
        model = models.StudyRecord
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields.values():
            i.widget.attrs.update({'class':'form-control'})