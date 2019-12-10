from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect,render,HttpResponse

class Login_check(MiddlewareMixin):
    white_list = ['/login/','/register/']
    def process_request(self,request):
        if request.path in self.white_list:
            return None
        else:
            if request.session.get('is_login'):
                return None
            else:
                return redirect('login')