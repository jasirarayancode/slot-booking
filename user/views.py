from django.shortcuts import render

from login.models import Login
from user.models import User

# Create your views here.
def post_user(request):
    if request.method=='POST':
        obj=User()
        obj.password = request.POST.get('psw')
        obj.age = request.POST.get('age')
        obj.name = request.POST.get('name')
        obj.contact_number = request.POST.get('phn')
        obj.save()

        ob = Login()
        ob.user_name = obj.name
        ob.password = obj.password
        ob.type = 'user'
        ob.u_id = obj.user_id
        ob.save()
        context={
            "msg":"Registered"
        }
        return render(request, 'user/user.html',context)
    return render(request, 'user/user.html')


def view_user(request):
    obj=User.objects.all()
    context={
        'x':obj
    }
    return render(request,'user/view_user.html',context)