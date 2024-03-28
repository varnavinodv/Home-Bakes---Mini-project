from django.shortcuts import render
from rating.models import Rating
from baker.models import Baker
# Create your views here.

def review(request):
    ss = request.session["u_id"]
    obk=""
    obb = Baker.objects.all()
    if request.method=="POST":
        obj=Rating()
        obj.customer_id=ss
        obj.baker_id=request.POST.get('nmb')
        obj.rating=request.POST.get('rating')
        obj.review=request.POST.get('rvw')
        obj.save()
        obk="success"
    context = {
        'a': obb,
        'msg':obk
    }
    return render(request,'rating/review.html',context)

def vwrwbkr(request):
    ss=request.session["u_id"]
    # if request.method=="POST":
    #     vv=request.POST.get('search')
    #     ob=Rating.objects.filter(baker__name__icontains=vv,baker_id=ss)
    #     context = {
    #         'x': ob
    #     }
    #     return render(request, 'rating/viewrevwbk.html', context)
    # else:
    #     ss = request.session["u_id"]
    obj=Rating.objects.filter(baker_id=ss)
    context={
        'x':obj
    }
    return render(request,'rating/viewrevwbk.html',context)
    # return render(request,'rating/viewrevwbk.html',context)


def vwrvwadm(request):
    if request.method=="POST":
        vv=request.POST.get('search')
        ob=Rating.objects.filter(baker__name__icontains=vv)
        context = {
            'x': ob
        }
        return render(request, 'rating/viewrevwadmin.html', context)
    else:
        obj=Rating.objects.all()
        context={
            'x':obj
        }
        return render(request,'rating/viewrevwadmin.html',context)
    # return render(request,'rating/viewrevwadmin.html',context)


def vwrvwcust(request):
    if request.method=="POST":
        vv=request.POST.get('search')
        ob=Rating.objects.filter(baker__name__icontains=vv)
        context = {
            'x': ob
        }
        return render(request, 'rating/viewrevwcust.html', context)
    else:
        obj=Rating.objects.all()
        context={
            'x':obj
        }
        return render(request,'rating/viewrevwcust.html',context)
    # return render(request,'rating/viewrevwcust.html',context)