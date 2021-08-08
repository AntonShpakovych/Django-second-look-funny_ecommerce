from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('categories/', include('categories.urls')),
    path('user/', include('user.urls'))
]
