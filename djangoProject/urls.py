from django.contrib import admin
from django.urls import path, include

from myApp.views import *

urlpatterns = [
    path('', include('myApp.urls')),
    path('admin/', admin.site.urls),
    ##path('aap/', include('app1.urls')),
]
