from django.conf.urls import url
from thorder import views


urlpatterns=[
    url('theme/(?P<idd>\w+)',views.thordr,name='them'),
    url('vwthordradm/',views.vwthordradm),
    url('vwthordrbk/',views.vwthordrbk),
    url('tacc/(?P<idd>\w+)',views.acpt,name='ta'),
    url('trej/(?P<idd>\w+)',views.rjct,name='rt'),
    url('delivered/(?P<idd>\w+)',views.delivered,name='dlv'),
    url('vwthordrcust/',views.vwthordrcust),
    url('cc/(?P<idd>\w+)',views.canc,name='can'),
    url('cdel/(?P<idd>\w+)',views.deli),

]
