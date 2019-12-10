from django.shortcuts import render, HttpResponse, redirect, reverse
from django.views import View
from app01 import myforms
from app01 import models
from app01.utils import md5_tools, pagination


# Create your views here.


class Login(View):

    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        if models.Userinfo.objects.filter(username=username, password=md5_tools.md5_encry(password, username)).exists():
            request.session['is_login'] = True
            request.session['username'] = username
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
            count_customer = models.Customer.objects.count()
            pa = pagination.Pagination(current_page_num, count_customer)
            customer_all = models.Customer.objects.filter(delete_status=False,consultant__isnull=True)[pa.data_start_fun():pa.data_end_fun()]
            # tag为1表示要看的公共客户
            tag = 1
        else:
            count_customer = models.Customer.objects.filter(
                consultant__username=request.session.get('username')).count()
            pa = pagination.Pagination(current_page_num, count_customer)
            customer_all = models.Customer.objects.filter(delete_status=False,consultant__username=request.session.get('username'))[
                           pa.data_start_fun():pa.data_end_fun()]
            # tag为2表示要看的个人客户
            tag = 2
        html = pa.html()
        search_val = request.GET.get('search')
        search_content = request.GET.get('search_content')
        if search_val and search_content:
            info = f'search={search_val}&search_content={search_content}&'
            count_customer = models.Customer.objects.filter(**{search_val: search_content}).count()
            pa = pagination.Pagination(current_page_num, count_customer, info)
            customer_all = models.Customer.objects.filter(**{search_val: search_content})[
                           pa.data_start_fun():pa.data_end_fun()]
            html = pa.html()
        return render(request, 'customer_info.html', {'customer_all': customer_all, 'html': html, 'tag': tag})

    def post(self, request):
        search_val = request.POST.get('search')
        search_content = request.POST.get('search_content')
        if search_val and search_content:
            customer_all = models.Customer.objects.filter(**{search_val: search_content})
            return render(request, 'customer_info.html', {'customer_all': customer_all})

        action = request.POST.get('action')
        self.choice = request.POST.getlist("choice")
        if hasattr(self,action):
            ret = getattr(self,action)(request,self.choice)
        return ret

    def trans_gts(self,request,choice):
        error_name = []
        for i in choice:
            if not models.Customer.objects.get(id=i).consultant:
                models.Customer.objects.filter(id=i).update(
                    consultant=models.Userinfo.objects.get(username=request.session.get('username'))
                )
            else:
                error_name.append(models.Customer.objects.get(id=i).name)
        return redirect('customer_info')

    def trans_stg(self,request,choice):
        models.Customer.objects.filter(id__in=choice).update(
            consultant=None
        )
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
            return redirect(request.GET.get('next'))
        else:
            return render(request, 'add_edit_customer.html', {'customerForm': customerForm})


class Del_Customer(View):
    def get(self, request, cid, tag):
        models.Customer.objects.filter(id=cid).update(
            delete_status=True
        )
        if tag == "1":
            return redirect('customer_info')
        else:
            return redirect('private_customer')


class Logout(View):
    def get(self, request):
        request.session.flush()
        return redirect('login')
