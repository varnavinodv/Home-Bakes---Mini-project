from django.http import HttpResponseRedirect
from django.shortcuts import render
from login.models import Login
# Create your views here.


def log(request):
    if request.method == "POST":
        eml = request.POST.get("mail")
        pasw = request.POST.get("psw")
        obj=Login.objects.filter(email=eml, password=pasw)
        print(len(obj))
        tp = ""
        for ob in obj:
            tp = ob.type
            uid = ob.u_id
            if tp == "admin":
                request.session["u_id"] = uid
                return HttpResponseRedirect('/temp/admin')
            elif tp == "baker":
                request.session["u_id"] = uid
                return HttpResponseRedirect('/temp/baker')
            elif tp == "customer":
                request.session["u_id"] = uid
                return HttpResponseRedirect('/temp/customer')
            objlist = "username or password incorrect...please try again...!"
            context={
                'msg': objlist,
            }
            return render(request, 'login/login.html',context)
    return render(request,'login/login.html')
