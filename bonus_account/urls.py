from django.conf.urls import url, include
from . import views



urlpatterns = [
    url('get_all/$', views.get_all_accounts),
    url('get_account/$', views.get_account),
    url('add_tras/$', views.add_tras),
    url('add_account/$', views.add_account),

]