from django.shortcuts import render
from customer.models import Customer
from login.models import Login
# from django.db.model import Q
from django.db.models import Q
# Create your views here.

def regcust(request):
    obk=""
    if request.method=="POST":
        a = request.POST.get('cphno')
        b = request.POST.get('ceml')
        obv = Customer.objects.filter(Q(phone_no=a) & (Q(email=b) | Q(phone_no=a) | Q(email=b)))
        if len(obv) > 0:
            obk = "User exist"
        else:
            obj=Customer()
            obj.name=request.POST.get('cnm')
            obj.age=request.POST.get('cage')
            obj.email=request.POST.get('ceml')
            obj.phone_no=request.POST.get('cphno')
            obj.house_name=request.POST.get('chnm')
            obj.post_office=request.POST.get('cpo')
            obj.pin_code=request.POST.get('cpin')
            obj.district=request.POST.get('district')
            obj.password=request.POST.get('cpsw')
            obj.save()

            obb=Login()
            obb.email=obj.email
            obb.password=obj.password
            obb.type="customer"
            obb.u_id=obj.customer_id
            obb.save()

            obk = "success"
    context = {
         'msg': obk
          }

    return render(request,'customer/regcust.html', context)



def vwupdtcust(request):
    ss=request.session["u_id"]
    obj=Customer.objects.filter(customer_id=ss)
    context={
        'x':obj
    }
    return render(request,'customer/viewupdateprofcust.html',context)



def updtcust(request,idd):
    obb=Customer.objects.get(customer_id=idd)
    context={
        'v':obb
    }
    if request.method=="POST":
        obj=Customer.objects.get(customer_id=idd)
        obj.name=request.POST.get('cnm')
        obj.age=request.POST.get('cage')
        obj.email=request.POST.get('ceml')
        obj.phone_no=request.POST.get('cphno')
        obj.house_name=request.POST.get('chnm')
        obj.post_office=request.POST.get('cpo')
        obj.pin_code=request.POST.get('cpin')
        obj.district=request.POST.get('district')
        obj.password=request.POST.get('cpwd')
        obj.save()

        obb = Login.objects.get(type='customer',u_id=request.session["u_id"])
        obb.email = obj.email
        obb.password = obj.password
        obb.u_id = obj.customer_id
        obb.save()
        return vwupdtcust(request)
    return render(request,'customer/updtcust.html',context)

def delete(request,idd):
    obj=Customer.objects.get(customer_id=idd)
    obj.delete()
    obb = Login.objects.get(u_id=request.session['u_id'], type='customer')
    obb.delete()
    return vwupdtcust(request)
