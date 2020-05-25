# from django.conf.urls import  include, url
# from django.contrib import admin




from django.contrib import admin
from django.urls import path
from django.conf.urls import include
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('health.urls')),
]