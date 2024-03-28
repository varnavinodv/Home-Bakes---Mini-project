from django.conf.urls import url
from baker import views


urlpatterns=[
    url('regbaker/',views.regbaker),
    url('mngbaker/',views.mngbaker),
    url('accept/(?P<idd>\w+)',views.accept),
    url('reject/(?P<idd>\w+)',views.reject),
    url('vwupdtbk/',views.vwupdtbk),
    url('updtbk/(?P<idd>\w+)',views.updtbk),
    url('delete/(?P<idd>\w+)',views.delete),



]