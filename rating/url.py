from django.conf.urls import url
from rating import views

urlpatterns=[
    url('rvw/',views.review),
    url('vwrvwbk/',views.vwrwbkr),
    url('vwrvwadm/',views.vwrvwadm),
    url('vwrvwcust/',views.vwrvwcust),
]
