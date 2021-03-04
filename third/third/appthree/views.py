from django.shortcuts import render
from appthree.models import User
# Create your views here.
def index(request):
    return render(request,'appthree/index.html')
def users(request):
    user_list=User.objects.order_by('firstname')
    user_dict={'users': user_list}
    return render(request,'appthree/users.html',context=user_dict)
