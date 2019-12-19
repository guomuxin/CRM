from django.shortcuts import render, HttpResponse, redirect, reverse
from django.views import View
from app01 import myforms
from django import forms
from django.forms import modelformset_factory
from app01 import models
from app01.utils import md5_tools, pagination
import json
from django.http.response import JsonResponse
from django.db import transaction
from rbac.serve import permission_insert
# Create your views here.


class Login(View):

    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        if models.Userinfo.objects.filter(username=username, password=md5_tools.md5_encry(password, username)).exists():
            request.session['name'] = username
            permission_insert.init_permission(request, username)
            return redirect('home')
        else:
            return redirect('login')


class Register(View):

    def get(self, request):
        registerForm = myforms.MyForm()
        return render(request, "register.html", {'registerForm': registerForm})

    def post(self, request):
        registerForm = myforms.MyForm(request.POST)
        if registerForm.is_valid():
            data = registerForm.cleaned_data
            data.pop("confirm_password")

            data['password'] = md5_tools.md5_encry(data['password'], data['username'])
            models.Userinfo.objects.create(
                **data
            )
            return redirect('login')
        else:
            return render(request, "register.html", {'registerForm': registerForm})


class Home(View):

    def get(self, request):
        return render(request, 'home.html')


class Customer_Info(View):

    def get(self, request):
        current_page_num = request.GET.get('page')
        if request.path == reverse('customer_info'):
            count_customer = models.Customer.objects.filter(delete_status=False, consultant__isnull=True).count()
            pa = pagination.Pagination(current_page_num, count_customer)
            customer_all = models.Customer.objects.filter(delete_status=False, consultant__isnull=True).order_by('-id')[
                           pa.data_start_fun():pa.data_end_fun()]
            # tag为1表示要看的公共客户
            tag = 1
        else:
            count_customer = models.Customer.objects.filter(
                consultant__username=request.session.get('username'), delete_status=False).count()
            pa = pagination.Pagination(current_page_num, count_customer)
            customer_all = models.Customer.objects.filter(delete_status=False, consultant__username=request.session.get(
                'username')).order_by('-id')[
                           pa.data_start_fun():pa.data_end_fun()]
            # tag为2表示要看的个人客户
            tag = 2
        html = pa.html()
        search_val = request.GET.get('search')
        search_content = request.GET.get('search_content')
        if search_val and search_content:
            info = f'search={search_val}&search_content={search_content}&'
            if tag == 1:
                count_customer = models.Customer.objects.filter(**{search_val: search_content}, delete_status=False,
                                                                consultant__isnull=True).count()
                pa = pagination.Pagination(current_page_num, count_customer, info)
                customer_all = models.Customer.objects.filter(**{search_val: search_content}, delete_status=False,
                                                              consultant__isnull=True).order_by('-id')[
                               pa.data_start_fun():pa.data_end_fun()]
            else:
                count_customer = models.Customer.objects.filter(**{search_val: search_content}, delete_status=False,
                                                                consultant__username=request.session.get(
                                                                    'username')).count()
                pa = pagination.Pagination(current_page_num, count_customer, info)
                customer_all = models.Customer.objects.filter(**{search_val: search_content}, delete_status=False,
                                                              consultant__username=request.session.get(
                                                                  'username')).order_by('-id')[
                               pa.data_start_fun():pa.data_end_fun()]
            html = pa.html()
        return render(request, 'customer_info.html', {'customer_all': customer_all, 'html': html, 'tag': tag})

    def post(self, request):
        search_val = request.POST.get('search')
        search_content = request.POST.get('search_content')
        if search_val and search_content:
            customer_all = models.Customer.objects.filter(**{search_val: search_content}).order_by('-id')
            return render(request, 'customer_info.html', {'customer_all': customer_all})

        action = request.POST.get('action')
        self.choice = request.POST.getlist("choice")
        if hasattr(self, action):
            ret = getattr(self, action)(request, self.choice)
        return ret

    def trans_gts(self, request, choice):
        error_name = []
        for i in choice:
            if not models.Customer.objects.get(id=i).consultant:
                models.Customer.objects.filter(id=i).update(
                    consultant=models.Userinfo.objects.get(username=request.session.get('username'))
                )
            else:
                error_name.append(models.Customer.objects.get(id=i).name)
        return redirect('customer_info')

    def trans_stg(self, request, choice):
        models.Customer.objects.filter(id__in=choice).update(
            consultant=None
        )
        return redirect('private_customer')

    def bulk_del(self, request, choice):
        models.Customer.objects.filter(id__in=choice).update(
            delete_status=True
        )
        if request.path == reverse('customer_info'):
            return redirect('customer_info')
        else:
            return redirect('private_customer')


class Add_Edit_Customer(View):

    def get(self, request, cid=None):

        customer_obj = None
        if cid:
            customer_obj = models.Customer.objects.filter(id=cid).first()
        customerForm = myforms.CustomerForm(instance=customer_obj)

        return render(request, 'add_edit_customer.html', {'customerForm': customerForm})

    def post(self, request, cid=None):

        customer_obj = models.Customer.objects.filter(id=cid).first()

        customerForm = myforms.CustomerForm(request.POST, instance=customer_obj)
        if customerForm.is_valid():
            customerForm.save()
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            else:
                return redirect('customer_info')
        else:
            return render(request, 'add_edit_customer.html', {'customerForm': customerForm})


class Del_Customer(View):
    def get(self, request, cid):
        models.Customer.objects.filter(id=cid).update(
            delete_status=True
        )
        next = request.GET.get("next")
        return redirect(next)


class Logout(View):
    def get(self, request):
        request.session.flush()
        return redirect('login')


class Consult_Record(View):
    def get(self, request, cid=None):
        # con_re_form = myforms.ConsultRecordForm()
        current_page_num = request.GET.get('page')
        if not current_page_num:
            current_page_num = 1
        if cid:
            count_record = models.ConsultRecord.objects.filter(customer__id=cid, delete_status=False,
                                                               consultant__username=request.session.get(
                                                                   'username')).count()
            pa = pagination.Pagination(current_page_num, count_record)
            consult_record_obj = models.ConsultRecord.objects.filter(customer__id=cid, delete_status=False,
                                                                     consultant__username=request.session.get(
                                                                         'username')).order_by('-id')[
                                 pa.data_start_fun():
                                 pa.data_end_fun()]
        else:
            count_record = models.ConsultRecord.objects.filter(delete_status=False,
                                                               consultant__username=request.session.get(
                                                                   'username')).count()
            pa = pagination.Pagination(current_page_num, count_record)
            consult_record_obj = models.ConsultRecord.objects.filter(delete_status=False,
                                                                     consultant__username=request.session.get(
                                                                         'username')).order_by('-id')[
                                 pa.data_start_fun():pa.data_end_fun()]
        search_val = request.GET.get('search')
        search_content = request.GET.get('search_content')
        seek_status_choices = (('A', '近期无报名计划'), ('B', '1个月内报名'), ('C', '2周内报名'), ('D', '1周内报名'),
                               ('E', '定金'), ('F', '到班'), ('G', '全款'), ('H', '无效'),)

        if search_val and search_content:
            for i in seek_status_choices:
                if search_content in i:
                    search_content = i[0]
            info = f'search={search_val}&search_content={search_content}&'
            count_record = models.ConsultRecord.objects.filter(**{search_val: search_content}, delete_status=False,
                                                               consultant__username=request.session.get(
                                                                   'username')).count()
            pa = pagination.Pagination(current_page_num, count_record, info)
            consult_record_obj = models.ConsultRecord.objects.filter(**{search_val: search_content},
                                                                     delete_status=False,
                                                                     consultant__username=request.session.get(
                                                                         'username')).order_by('-id')[
                                 pa.data_start_fun():pa.data_end_fun()]
        html = pa.html()
        return render(request, 'consult_record.html', {'consult_record_obj': consult_record_obj, 'html': html})


class Consult_Record_Edit(View):
    def get(self, request, cid=None):
        if cid:
            consult_re_obj = models.ConsultRecord.objects.filter(id=cid)[0]
            consult_re_form = myforms.ConsultRecordForm(request, instance=consult_re_obj)
        else:
            consult_re_form = myforms.ConsultRecordForm(request)
        return render(request, 'add_edit_consult_record.html', {'consult_re_form': consult_re_form})

    def post(self, request, cid=None):
        if cid:
            consult_re_obj = models.ConsultRecord.objects.filter(id=cid)[0]
            consult_re_form = myforms.ConsultRecordForm(request, request.POST, instance=consult_re_obj)
        else:
            consult_re_form = myforms.ConsultRecordForm(request, request.POST)

        if consult_re_form.is_valid():
            consult_re_form.save()
            if request.path == reverse("consult_record_add"):
                return redirect('consult_record')
            else:
                return redirect(request.GET.get('next'))
        else:
            return render(request, 'add_edit_consult_record.html', {'consult_re_form': consult_re_form})


class Consult_Record_Del(View):
    def get(self, request, cid):
        models.ConsultRecord.objects.filter(id=cid).update(
            delete_status=True
        )
        return redirect(request.GET.get('next'))


class EnrollmentInfo(View):
    def get(self, request):
        enrollment_all = models.Enrollment.objects.all().filter(delete_status=False).order_by('-id')
        return render(request, 'enrollment.html', {'enrollment_all': enrollment_all})


class EnrollmentAddEdit(View):
    def get(self, request, cid=None):
        if cid:
            enrollment_obj = models.Enrollment.objects.filter(id=cid)[0]
            enrollment_form = myforms.EnrollmentForm(instance=enrollment_obj)
        else:
            enrollment_form = myforms.EnrollmentForm()
        return render(request, 'enrollment_add_edit.html', {'enrollment_form': enrollment_form})

    def post(self, request, cid=None):
        if cid:
            enrollment_obj = models.Enrollment.objects.filter(id=cid)[0]
            enrollment_form = myforms.EnrollmentForm(request.POST, instance=enrollment_obj)
        else:
            enrollment_form = myforms.EnrollmentForm(request.POST)

        if enrollment_form.is_valid():
            enrollment_form.save()
            if request.path == reverse("enrollment_add"):
                return redirect('enrollment_info')
            else:
                return redirect(request.GET.get('next'))
        else:
            return render(request, 'enrollment_add_edit.html', {'enrollment_form': enrollment_form})


class EnrollmentDel(View):
    def get(self, request, cid):
        models.Enrollment.objects.filter(id=cid).update(
            delete_status=True
        )
        return redirect(request.GET.get('next'))


class CourseRecordInfo(View):
    def get(self, request):
        coureRecord_all = models.CourseRecord.objects.all().order_by('-id')
        return render(request, 'course_record.html', {'coureRecord_all': coureRecord_all})

    def post(self, request):
        action = request.POST.get('action')
        cids = json.loads(request.POST.get('cids_list'))
        if hasattr(self, action):
            ret = getattr(self, action)(request, cids)
        return ret

    def bulk_add_studyRecord(self, request, cids):
        try:
            with transaction.atomic():
                for id in cids:
                    print(id)
                    class_id = models.CourseRecord.objects.get(id=id).re_class.id
                    print(class_id)
                    students = models.Customer.objects.filter(class_list__id=class_id,status="studying")
                    print(students)
                    for j in students:
                        models.StudyRecord.objects.create(
                            course_record=models.CourseRecord.objects.get(id=id),
                            student=j

                        )
                status = {"check": 0, "error": None}

        except Exception as e:
            print(e)
            status = {"check": 1, "error": "添加错误"}
        return JsonResponse(status)

class CourseRecordAddEdit(View):
    def get(self, request, cid=None):
        if cid:
            course_obj = models.CourseRecord.objects.filter(id=cid)[0]
            courseRecord_form = myforms.CourseRecordForm(instance=course_obj)
        else:
            courseRecord_form = myforms.CourseRecordForm()
        return render(request, 'course_record_add_edit.html', {'courseRecord_form': courseRecord_form})

    def post(self, request, cid=None):
        if cid:
            course_obj = models.CourseRecord.objects.filter(id=cid)[0]
            courseRecord_form = myforms.CourseRecordForm(request.POST, instance=course_obj)
        else:
            courseRecord_form = myforms.CourseRecordForm(request.POST)

        if courseRecord_form.is_valid():
            courseRecord_form.save()
            if request.path == reverse("coure_record_add"):
                return redirect('coure_record_info')
            else:
                return redirect(request.GET.get('next'))
        else:
            return render(request, 'course_record_add_edit.html', {'courseRecord_form': courseRecord_form})


class CourseRecordDel(View):
    def get(self, request, cid):
        models.CourseRecord.objects.filter(id=cid).delete()
        return redirect(request.GET.get('next'))


class StudyRecordInfo(View):
    def get(self, request):
        studyForm = modelformset_factory(models.StudyRecord, myforms.StudyRecordForm, extra=0)
        return render(request, 'study_record.html', {'studyForm': studyForm})

    # def post(self, request):
    #     studyForm = modelformset_factory(models.StudyRecord, myforms.StudyRecordForm, extra=0)
    #     studyForm = studyForm(request.POST)
    #     if studyForm.is_valid():
    #         studyForm.save()
    #     ;;return redirect('studyRecord_info')