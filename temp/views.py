from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'temp/home.html')

def main_home(request):
    return render(request,'temp/main_home.html')

def admin(request):
    return render(request,'temp/admin.html')

def baker(request):
    return render(request,'temp/baker.html')


def customer(request):
    return render(request,'temp/customer.html')
