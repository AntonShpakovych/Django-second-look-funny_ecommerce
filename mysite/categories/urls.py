from django.urls import path
from django.urls import path
from . import views


urlpatterns = [
    path('', views.slidebar, name='slide-bar'),
    path('laptop', views.LaptopListView.as_view(), name='laptop'),
    path('table-pc', views.PCListView.as_view(), name='table-pc'),
    path('mobile', views.MobileListView.as_view(), name='mobile'),
    path('laptop/<int:pk>', views.LaptopMoreDetails.as_view(), name='more-details')
]
