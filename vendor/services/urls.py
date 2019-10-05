from django.urls import path, re_path
from services import views as ser_views

urlpatterns = [
    path('', ser_views.index, name= 'index'),
    path('signup/',ser_views.signup, name='signup'),
    path('vendor_signup/',ser_views.vendor_signup, name='vendor_signup'),
    path('customer_signup/',ser_views.customer_signup, name='customer_signup'),
    path('services/',ser_views.services, name='services'),
    path('view_profile/',ser_views.view_profile, name='view_profile'),
    path('update_profile/',ser_views.update_profile, name='update_profile'),
    path('deactivate-account/',ser_views.deactivate_account, name='deactivate-account'),
    re_path(r'^password/$', ser_views.change_password, name='change_password'),
    re_path(r'^services/(?P<id>\d+)/(?P<service_name>[\w ]+)/$', ser_views.service_info, name='services'),
    #re_path(r'^services/(?P<id>\d+)/(?P<service_name>[\w ]+)/(?P<service>\d+)/(?P<sub_service_name>[\w ]+)/$', ser_views.vendors, name='services'),

    

]
