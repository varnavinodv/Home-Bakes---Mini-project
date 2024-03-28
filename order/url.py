from django.conf.urls import url
from order import views


urlpatterns=[
    url('ordr/(?P<idd>\w+)',views.ordr),
    url('vwordrbk/',views.vwordrbk),
    url('accept/(?P<idd>\w+)',views.accept),
    url('reject/(?P<idd>\w+)',views.reject),
    url('delivered/(?P<idd>\w+)',views.delivered),
    url('vwordradm/',views.vwordradm),
    url('vwordrcust/',views.vwordrcust),
    url('cancel/(?P<idd>\w+)',views.cancel),
    url('dd/(?P<idd>\w+)',views.delivery)

]
