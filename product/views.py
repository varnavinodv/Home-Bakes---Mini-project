from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from product.models import Product
# Create your views here.
from django.http import HttpResponseRedirect
def addcak(request):
    ss = request.session["u_id"]
    obk=""
    if request.method=="POST":
        obj=Product()
        obj.baker_id=ss
        obj.cake_name=request.POST.get('cnm')
        # obj.image1=request.POST.get('imgf')
        myfile = request.FILES['imgf']
        fs = FileSystemStorage()
        filname = fs.save(myfile.name, myfile)
        obj.image1 = myfile.name
        obj.image2=''
        obj.image3=''
        try:
            # obj.image2=request.POST.get('imgs')
            myfile = request.FILES['imgs']
            fs = FileSystemStorage()
            filname = fs.save(myfile.name, myfile)
            obj.image2 = myfile.name

            # obj.image3=request.POST.get('imgt')
            myfile = request.FILES['imgt']
            fs = FileSystemStorage()
            filname = fs.save(myfile.name, myfile)
            obj.image3 = myfile.name
        except:
                pass
        obj.flavour=request.POST.get('flv')
        obj.price=request.POST.get('prc')
        obj.type=request.POST.get('typ')
        obj.save()
        obk = "success"
    context = {
            'msg': obk
        }
    return render(request,'product/addcake.html',context)

def updtcak(request,idd):
    ss = request.session["u_id"]
    obb=Product.objects.get(product_id=idd)
    context={
        'v':obb
    }
    if request.method=="POST":
        obj=Product.objects.get(product_id=idd)
        obj.baker_id=ss
        obj.cake_name=request.POST.get('cnm')
        try:
           # obj.image1=request.POST.get('imgf')
           myfile = request.FILES['imgf']
           fs = FileSystemStorage()
           filename = fs.save(myfile.name, myfile)
           obj.image1 = myfile.name
           # obj.image2=request.POST.get('imgs')
           myfile=request.FILES['imgs']
           fs=FileSystemStorage()
           filename=fs.save(myfile.name,myfile)
           obj.image2=myfile.name
           # obj.image3=request.POST.get('imgt')
           myfile=request.FILES['imgt']
           fs=FileSystemStorage()
           filename=fs.save(myfile.name,myfile)
           obj.image3=myfile.name
        except:
               pass
        obj.flavour=request.POST.get('flv')
        obj.price=request.POST.get('prc')
        obj.type=request.POST.get('typ')
        obj.save()
        return HttpResponseRedirect('/product/vwprdctbk/#xx')
    return render(request,'product/updtcake.html',context)

def delete(request,idd):
    obj=Product.objects.get(product_id=idd)
    obj.delete()
    return vwprdctbk(request)


def vwprdctadm(request):
    if request.method=='POST':

        act=request.POST.get('action')
        if act =='search':
            vv=request.POST.get('search')
            obj=Product.objects.filter(Q(cake_name__icontains=vv) | Q(baker__name__icontains= vv))
            context={
                'x':obj,
                'se': vv
            }
        elif act=='Simple cakes':
            vv = request.POST.get('search')
            obj = Product.objects.filter((Q(cake_name__icontains=vv) | Q(baker__name__icontains=vv)) & Q(type='simple'))
            context = {
                'x': obj,
                'se':vv
            }
        elif act=='Theme cakes':
            vv = request.POST.get('search')
            obj = Product.objects.filter((Q(cake_name__icontains=vv) | Q(baker__name__icontains=vv)) & Q(type='Theme'))
            context = {
                'x': obj,
                'se':vv
            }
            return render(request,'product/viewprdctadmin.html',context)
    else:
        obj=Product.objects.all()
        context={
        'x':obj
        }
    return render(request,'product/viewprdctadmin.html',context)
    # else:
    #      obj=Product.objects.all()
    #      context={
    #          'x':obj
    #      }
    # return render(request,'product/viewprdctadmin.html',context)

def vwprdctbk(request):
    ss=request.session["u_id"]
    if request.method=='POST':

        act=request.POST.get('action')
        if act =='search':
            vv=request.POST.get('search')
            obj=Product.objects.filter(Q(cake_name__icontains=vv) | Q(baker__name__icontains= vv),baker_id=ss)
            context={
                'x':obj,
                'se': vv
            }
            return render(request, 'product/viewupdtprdtbk.html', context)
        elif act=='Simple cakes':
            vv = request.POST.get('search')
            obj = Product.objects.filter((Q(cake_name__icontains=vv) | Q(baker__name__icontains=vv)) & Q(type='simple'),baker_id=ss)
            context = {
                'x': obj,
                'se':vv
            }
            return render(request, 'product/viewupdtprdtbk.html', context)
        elif act=='Theme cakes':
            vv = request.POST.get('search')
            obj = Product.objects.filter((Q(cake_name__icontains=vv) | Q(baker__name__icontains=vv)) & Q(type='Theme'),baker_id=ss)
            context = {
                'x': obj,
                'se':vv
            }
            return render(request,'product/viewupdtprdtbk.html',context)
    else:
        obj=Product.objects.filter(baker_id=ss)
        context={
        'x':obj
        }
    return render(request,'product/viewupdtprdtbk.html',context)
    # return render(request, 'product/viewupdtprdtbk.html',context)

from django.db.models import Q
def vwprdctcus(request):
    if request.method=='POST':

        act=request.POST.get('action')
        if act =='search':
            vv=request.POST.get('search')
            obj=Product.objects.filter(Q(cake_name__icontains=vv) | Q(baker__name__icontains= vv))
            context={
                'x':obj,
                'se': vv
            }
        elif act=='Simple cakes':
            vv = request.POST.get('search')
            obj = Product.objects.filter((Q(cake_name__icontains=vv) | Q(baker__name__icontains=vv)) & Q(type='simple'))
            context = {
                'x': obj,
                'se':vv
            }
        elif act=='Theme cakes':
            vv = request.POST.get('search')
            obj = Product.objects.filter((Q(cake_name__icontains=vv) | Q(baker__name__icontains=vv)) & Q(type='Theme'))
            context = {
                'x': obj,
                'se':vv
            }
            return render(request,'product/viewprdctcust.html',context)
    else:
        obj=Product.objects.all()
        context={
        'x':obj
        }
    return render(request,'product/viewprdctcust.html',context)


