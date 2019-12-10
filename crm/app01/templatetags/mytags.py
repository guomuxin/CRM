from django import template
from django.urls import reverse
from django.http.request import QueryDict
register = template.Library()

@register.simple_tag
def url_handle(url_name,cid,request):
    customer_qd = QueryDict(mutable=True)
    customer_qd['next'] = request.get_full_path()
    next = customer_qd.urlencode()

    old_url = reverse(url_name,args=(cid,))
    url_final = old_url + "?" + next
    return url_final