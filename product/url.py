from django.conf.urls import url
from product import views


urlpatterns=[
    url('addcak/',views.addcak),
    url('updtcak/(?P<idd>\w+)',views.updtcak,name='up'),
    url('vwprdctadm/',views.vwprdctadm),
    url('vwprdctbk/',views.vwprdctbk),
    # url('updtck/',views.vwprdctbk),
    url('delete/(?P<idd>\w+)',views.delete,name='dd'),
    url('vwprdctcus/',views.vwprdctcus),

]
