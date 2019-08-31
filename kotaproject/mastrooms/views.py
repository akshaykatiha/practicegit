from django.shortcuts import get_object_or_404, render, redirect
from .models import User, Owner, Room, Tenant
from django.core.paginator import Paginator

def index(request):
    return render(request,'mastrooms/index.html')

def about_us(request):
    return render(request,'mastrooms/about_us.html')

def register_property(request):
    return render(request,'mastrooms/register_property.html')
 
def faq(request):
    return render(request,'mastrooms/faq.html')

def terms_and_conditions(request):
    return render(request,'mastrooms/terms_and_conditions.html')

def privacy_policy(request):
    return render(request,'mastrooms/privacy_policy.html')

def instructions(request):
    return render(request, 'mastrooms/instructions.html')

def rooms(request):
    room_list = Room.objects.all().order_by("rent")
    #owner_id = Room.objects.get(owner=id)
    #contact = User.objects.get(pk=id)
    #display_contact = contact.phone
    paginator = Paginator(room_list, 6)
    page = request.GET.get('page')
    room = paginator.get_page(page)
    count = paginator.get_page(page)
    context = {
        'room' : room,
        'count' : count,
        #'phone' : display_contact,
    }
    return render (request, 'mastrooms/rooms.html', context)

def room_detail(request, id, name):
    room = Room.objects.get(id=id)
    context = {
        'room' : room,
    }
    return render(request, 'mastrooms/room_detail.html', context)