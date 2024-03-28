from django.http import HttpResponseRedirect
from django.shortcuts import render
from order.models import Order
from product.models import Product
from payment.models import Payment
from customer.models import Customer
from datetime import datetime
# Create your views here.

def ordr(request,idd):
    ss=request.session["u_id"]
    obk = Customer.objects.get(customer_id=ss)
    obb = Product.objects.get(product_id=idd)
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d")
    context = {
        'a': obb,
        'b':obk,
        'dt': date_time,
    }
    if request.method=="POST":
        obj=Order()
        obj.customer_id=ss
        obj.product_id=idd
        obj.baker_id=obb.baker_id
        obj.shape=request.POST.get('shp')
        obj.cake_count=request.POST.get('cnt')
        obj.weight=request.POST.get('wgt')
        obj.tier=request.POST.get('tr')
        obj.delivery_date=request.POST.get('dte')
        obj.delivery_time=request.POST.get('tme')
        obj.wishes=request.POST.get('wss')
        # obj.total_price=request.POST.get('tprc')
        # obj.delivery_charge="60"
        obj.status='pending'
        obj.save()
        return HttpResponseRedirect('/product/vwprdctcus/#ee')
    return render(request,'order/order.html',context)


def vwordrbk(request):
    ss=request.session["u_id"]
    obj=Order.objects.filter(baker_id=ss)
    context={
        'x':obj
    }
    return render(request,'order/vieworderbk.html',context)

def accept(request,idd):
    obj=Order.objects.get(order_id=idd)
    obj.status="Accepted"
    obj.save()
    # return vwordrbk(request)
    return HttpResponseRedirect('/order/dd/'+str(obj.order_id))
    # return render(request,'order/delivery.html')

def reject(request,idd):
    obj=Order.objects.get(order_id=idd)
    obj.status="Rejected"
    obj.save()
    return vwordrbk(request)

def delivered(request,idd):
    obj=Order.objects.get(order_id=idd)
    obj.status="Delivered"
    obj.save()
    return vwordrbk(request)

def vwordradm(request):
    obj=Order.objects.all()
    context={
        'x':obj
    }
    return render(request,'order/viewordradmin.html',context)


def vwordrcust(request):
    ss=request.session["u_id"]
    obj=Order.objects.filter(customer_id=ss)
    context={
        'x':obj
    }
    return render(request,'order/viewordercust.html',context)

def cancel(request,idd):
    obj=Order.objects.get(order_id=idd)
    obj.status="Cancelled"
    obj.save()
    return vwordrcust(request)

# from payment.models import Payment


def delivery(request,idd):
    if request.method=='POST':
        obj=Order.objects.get(order_id=idd)
        obj.delivery_charge = request.POST.get('cvv')
        xx=float(obj.weight)* int(obj.cake_count)
        pp=obj.product.price
        obj.total_price=float(xx) * int(pp) + int(obj.delivery_charge)
        obj.save()
        return vwordrbk(request)
    return render(request,'order/delivery.html')
