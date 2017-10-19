from django.conf.urls import url
from . import views

app_name = 'ulam'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'ulam/upload/$',views.FoodCreate.as_view(), name='ulam-upload'),
    url(r'ulam/(?P<pk>[0-9]+)/$',views.FoodUpdate.as_view(), name='ulam-update'),
    url(r'ulam/(?P<pk>[0-9]+)/delete/$',views.FoodDelete.as_view(), name='ulam-delete'),
]
 
