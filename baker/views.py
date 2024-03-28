from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from baker.models import Baker
from login.models import Login
from django.db.models import Q

# Create your views here.

def regbaker(request):
    obk=""
    if request.method=="POST":
        a = request.POST.get('bphno')
        b = request.POST.get('beml')
        obv = Baker.objects.filter(Q(phone_no=a) & (Q(email=b) | Q(phone_no=a) | Q(email=b)))
        if len(obv) > 0:
            obk = "User exist"
        else:
            obj=Baker()
            obj.name=request.POST.get('bnm')
            obj.age=request.POST.get('bage')
            obj.email=request.POST.get('beml')
            obj.phone_no=request.POST.get('bphno')
            obj.house_name=request.POST.get('bhnm')
            obj.post_office=request.POST.get('bpo')
            obj.pin_code=request.POST.get('bpin')
            obj.district=request.POST.get('district')
            # obj.liscense=request.POST.get('liscense')
            myfile = request.FILES['liscense']
            fs = FileSystemStorage()
            filname = fs.save(myfile.name, myfile)
            obj.liscense = myfile.name
            obj.password=request.POST.get('psw')
            obj.status="Pending"
            obj.save()
            obk="success"
    context={
        'msg':obk
        }
    return render(request, 'baker/regbaker.html',context)

def mngbaker(request):
    obj=Baker.objects.all()
    context={
        'x':obj
    }
    return render(request, 'baker/managebakeradmin.html',context)

def accept(request,idd):
    obj=Baker.objects.get(baker_id=idd)
    obj.status="Accepted"
    obj.save()
    obb = Login()

    obb.email = obj.email
    obb.password = obj.password
    obb.type = "baker"
    obb.u_id = obj.baker_id
    obb.save()
    return mngbaker(request)

def reject(request,idd):
    obj=Baker.objects.get(baker_id=idd)
    obj.status="Rejected"
    obj.save()
    return mngbaker(request)



def vwupdtbk(request):
    ss=request.session["u_id"]
    obj=Baker.objects.filter(baker_id=ss)
    context={
        'x': obj
    }
    return render(request, 'baker/viewupdateprofbk.html',context)


def updtbk(request,idd):
    obb=Baker.objects.get(baker_id=idd)
    context={
        'v':obb
    }
    if request.method=="POST":
        obj=Baker.objects.get(baker_id=idd)
        obj.name=request.POST.get('bnm')
        obj.age=request.POST.get('bage')
        obj.email=request.POST.get('beml')
        obj.phone_no=request.POST.get('bphno')
        obj.house_name=request.POST.get('bhnm')
        obj.post_office=request.POST.get('bpo')
        obj.pin_code=request.POST.get('bpin')
        obj.district=request.POST.get('district')
        # obj.liscense=request.POST.get('liscense')
        # obj.liscense=''
        try:
            myfile = request.FILES['liscense']
            fs = FileSystemStorage()
            filname=fs.save(myfile.name,myfile)
            obj.liscense=myfile.name
        except:
              pass
        obj.password=request.POST.get('pwd')
        obj.save()

        obb = Login.objects.get(u_id=request.session["u_id"],type='baker')
        obb.email = obj.email
        obb.password = obj.password
        obb.u_id=obj.baker_id
        obb.save()
        return vwupdtbk(request)
    return render(request, 'baker/updtbaker.html',context)

def delete(request,idd):
    obj=Baker.objects.get(baker_id=idd)
    obj.delete()
    obb=Login.objects.get(u_id=idd,type='baker')
    obb.delete()
    return vwupdtbk(request)


