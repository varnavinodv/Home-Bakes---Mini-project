from django.conf.urls import url
from temp import views

urlpatterns=[
    url('home/',views.home),
    url('main/',views.main_home),
    url('admin/',views.admin),
    url('baker/',views.baker),
    url('customer/',views.customer),
]