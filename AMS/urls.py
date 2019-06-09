from django.conf.urls import url
from AMS import views
from AMS.views import addAsset, addLocation, main, editAsset,Login, LocationList,ApprovalList

urlpatterns = [
    url('login', Login.as_view(), name='login'),
    url('assets', main.as_view(), name='main'),
    url('add', addAsset.as_view(), name='add'),
    url ('location',addLocation.as_view(),name='location'),
    url('search',views.Search,name='search'),
    url(r'^asset/(?P<pk>\d+)/',editAsset.as_view(),name='modify'),
    url('Llist', LocationList.as_view(), name='Llist'),
    url('pending', ApprovalList.as_view(), name='pending'),
    url('specialsearch',views.SpecialSearch,name='specialsearch'),
    url(r'^approve/(?P<pk>\d+)/',views.approve,name='approve')
]