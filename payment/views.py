from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from payment.models import Payment
import datetime
from order.models import Order
from thorder.models import Theme
# Create your views here.

def pay(request,idd):
    ss = request.session["u_id"]
    obb=Order.objects.get(order_id=idd)
    context={
        'a':obb
    }
    if request.method=="POST":
        obj=Payment()
        obj.customer_id=ss
        obj.baker_id=obb.baker_id
        obj.order_id=idd
        obj.card_holder=request.POST.get('chnm')
        obj.cvv=request.POST.get('cvv')
        obj.date=datetime.datetime.today()
        obj.amount=request.POST.get('tprc')
        obj.status="paid"
        obj.save()
        obb=Order.objects.get(order_id=idd)
        obb.status="Paid"
        obb.save()
        return HttpResponseRedirect('/payment/bill/'+str(obj.order_id))
    return render(request,'payment/payment.html',context)


def vwpay(request):
    ss=request.session["u_id"]
    obj=Payment.objects.filter(baker_id=ss)
    context={
        'x':obj
    }
    return  render(request,'payment/viewpaybk.html',context)


from payment.models import Thpayment

def thpy(request,idd):
    ss = request.session["u_id"]
    obb = Theme.objects.get(theme_id=idd)
    context = {
        'a': obb
    }
    if request.method=="POST":
        obj=Thpayment()
        obj.customer_id=ss
        obj.baker_id=obb.baker_id
        obj.theme_id=idd
        obj.card_holder=request.POST.get('chnm')
        obj.cvv=request.POST.get('cvv')
        obj.date=datetime.datetime.today()
        obj.amount=request.POST.get('tprc')
        obj.status="paid"
        obj.save()
        obb=Theme.objects.get(theme_id=idd)
        obb.status="paid"
        obb.save()
        return HttpResponseRedirect('/payment/tb/' + str(obj.theme_id))
    return render(request,'payment/themepay.html',context)


def thvwpay(request):
    ss=request.session["u_id"]
    obj=Thpayment.objects.filter(baker_id=ss)
    context={
        'x':obj
    }
    return  render(request,'payment/viewthpay.html',context)

#Bill generate

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
#To Generate Checklist pdf
# def index(request,idd,pid):
from home_bakes import settings


def index(request, idd):
    # return HttpResponse('hello')
    # print("helloooooooooo")
    ob = Order.objects.get(order_id=idd)
    context = {
        'ok': ob,
    }
    template_path = 'payment/bill.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="bill.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    fpath = str(settings.BASE_DIR) + str(settings.STATIC_URL) + str(ob.customer_id) + ".pdf"

    # create a pdf
    outfile = open(fpath, "w+b")
    # pisa_status = pisa.CreatePDF(
    #     html, dest=response)
    pisa_status = pisa.CreatePDF(html, dest=outfile)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    # return response
    return render(request, 'payment/bill.html', context)

#bill2


def index1(request, idd):
    # return HttpResponse('hello')
    # print("helloooooooooo")
    ob = Theme.objects.get(theme_id=idd)
    context = {
        'ok': ob,
    }
    template_path = 'payment/thbill.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="bill.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    fpath = str(settings.BASE_DIR) + str(settings.STATIC_URL) + str(ob.customer_id) + ".pdf"

    # create a pdf
    outfile = open(fpath, "w+b")
    # pisa_status = pisa.CreatePDF(
    #     html, dest=response)
    pisa_status = pisa.CreatePDF(html, dest=outfile)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    # return response
    return render(request, 'payment/thbill.html', context)


