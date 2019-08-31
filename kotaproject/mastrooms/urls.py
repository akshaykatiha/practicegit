from django.urls import path, re_path
from . import views 
#app_name = 'mastrooms'
urlpatterns = [
    
    path('',views.index,name='index'),
    path('about_us/',views.about_us,name='about_us'),
    path('register_property/',views.register_property,name='register_property'),
    path('faq/',views.faq,name='faq'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('terms_and_conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    re_path(r'^rooms/(?P<id>\d+)/(?P<name>[\w ]+)/$', views.room_detail, name='rooms'),
    path('rooms/', views.rooms, name="rooms"),
    path('instructions', views.instructions, name="instructions"),

]