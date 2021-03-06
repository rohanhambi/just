from django.conf.urls import  include, url
from django.contrib.auth import views as auth_views
from . import views

# Make sure to end each URL pattern with '/?$' to make sure the end of the url
# properly handles omitting the trailing slash.
urlpatterns = [
    url(r'login/?$', views.login_view, name='login'),
    url(r'logout/?$', views.logout_view, name='logout'),
    url(r'schedule/?$', views.schedule, name='schedule'),
    url(r'prescriptions/?$', views.prescriptions, name='prescriptions'),
    url(r'messages/?$', views.messages, name='messages'),
    url(r'messages/(\d+)/?$', views.conversation, name='conversation'),
    url(r'delete_prescription/(\d+)/?$', views.delete_prescription, name='delete_prescription'),
    url(r'edit_prescription/(\d+)?/?$', views.prescription_form, name='edit_prescription'),
    url(r'add_prescription/?$', views.add_prescription_form, name='add_prescription'),
    url(r'delete_appointment/(\d+)/?$', views.delete_appointment, name='delete_appointment'),
    url(r'edit_appointment/(\d+)?/?$', views.appointment_form, name='edit_appointment'),
    url(r'add_appointment/?$', views.add_appointment_form, name='add_appointment'),
    url(r'add_group/?$', views.add_group, name='add_group'),
    url(r'users/(\d+)/?$', views.medical_information, name='medical_information'),
    url(r'users/me/?$', views.my_medical_information, name='my_medical_information'),
    url(r'signup/?$', views.signup, name='signup'),
    url(r'users/(\d+)/info.json/?$', views.export, name='export'),
    url(r'users/me/info.json/?$', views.export_me, name='export_me'),
    url(r'users/?$', views.users, name='users'),
    url(r'logs/?$', views.logs, name='logs'),
    url(r'^/?$', views.home, name='home'),
]