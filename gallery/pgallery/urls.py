from django.conf import settings
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.index,name='index.html'),
    url(r'^search/', views.search_results, name='search_results')

]