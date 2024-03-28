from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from thorder.models import Theme
from product.models import Product
from customer.models import Customer
from datetime import datetime

# Create your views here.

def thordr(request,idd):
    ss = request.session["u_id"]
    obk = Customer.objects.get(customer_id=ss)
    obb = Product.objects.get(product_id=idd)
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d")

    context={
        'a': obb,
        'b' :obk,
        'dt': date_time,

    }
    if request.method=="POST":
        obj=Theme()
        obj.customer_id=ss
        obj.baker_id=obb.baker_id
        obj.product_id=idd
        obj.shape=request.POST.get('shape')
        obj.cake_count=request.POST.get('ct')
        obj.weight=request.POST.get('wt')
        obj.tier=request.POST.get('tire')
        obj.wishes=request.POST.get('ws')
        obj.desciption=request.POST.get('dcr')
        # obj.photo=request.POST.get('rfpic')
        obj.photo=''
        try:
            myfile = request.FILES['rfpic']
            fs = FileSystemStorage()
            filname = fs.save(myfile.name, myfile)
            obj.photo = myfile.name
        except:

              pass
        obj.delivery_date=request.POST.get('de')
        obj.delivery_time=request.POST.get('te')
        obj.amount=request.POST.get('rt')
        # obj.total_price=request.POST.get('tr')
        obj.status="pending"
        # obj.delivery_charge=request.POST.get('ch')
        obj.save()
        return HttpResponseRedirect('/product/vwprdctcus/#ee')
    return render(request, 'thorder/themeo.html',context)


def  vwthordradm(request):
    obj=Theme.objects.all()
    context={
        'x':obj
    }
    return render(request,'thorder/viewthemeorderadmin.html',context)



def vwthordrbk(request):
    ss=request.session["u_id"]
    obj=Theme.objects.filter(baker_id=ss)
    context={
        'x':obj
    }
    return render(request,'thorder/viewthemeorderbk.html',context)


def acpt(request,idd):
    obj=Theme.objects.get(theme_id=idd)
    obj.status="Accepted"
    obj.save()
    return HttpResponseRedirect('/theme/cdel/'+ str(obj.theme_id))
    # return vwthordrbk(request)

def rjct(request,idd):
    obj=Theme.objects.get(theme_id=idd)
    obj.status="Rejected"
    obj.save()
    return vwthordrbk(request)

def delivered(request,idd):
    obj=Theme.objects.get(theme_id=idd)
    obj.status="Delivered"
    obj.save()
    return vwthordrbk(request)



def vwthordrcust(request):
    ss = request.session["u_id"]
    obj=Theme.objects.filter(customer_id=ss)
    context={
        'x':obj
    }
    return render(request,'thorder/viewthemeordercust.html',context)

def canc(request,idd):
    obj=Theme.objects.get(theme_id=idd)
    obj.status="Cancelled"
    obj.save()
    return vwthordrcust(request)


def deli(request,idd):
    if request.method=='POST':
        obj=Theme.objects.get(theme_id=idd)
        obj.delivery_charge = request.POST.get('ch')
        xx = float(obj.weight) * int(obj.cake_count)
        pk=obj.product.price
        obj.total_price=float(xx) * int(pk) + int(obj.delivery_charge)
        obj.save()
        return vwthordrbk(request)
    return render(request,'thorder/deliveryth.html')