from django.conf.urls import url
from customer import views

urlpatterns=[
    url('regcust/',views.regcust),
    url('vwupdtcust/',views.vwupdtcust),
    url('updtcust/(?P<idd>\w+)',views.updtcust),
    url('delete/(?P<idd>\w+)',views.delete),

]