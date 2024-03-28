from django.conf.urls import url
from payment import views


urlpatterns=[
    url('pay/(?P<idd>\w+)',views.pay),
    url('vwpy/',views.vwpay),

    url('thp/(?P<idd>\w+)',views.thpy,name='thpy'),
    url('view/',views.thvwpay),

    url('bill/(?P<idd>\w+)', views.index),
    url('tb/(?P<idd>\w+)',views.index1)

]