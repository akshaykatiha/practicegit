from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import (
    User,
    Service,
    SubService,
    VendorService,
)
from .forms import VendorForm, CustomerForm, UpdateProfile
from django.contrib.auth import authenticate
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.db import connection, transaction
from django.db.models import Q



# Create your views here.
def index(request):
    context = {}
    template_name = 'services/index.html'
    return render(request, template_name=template_name, context=context)


def signup(request):
    template_name = 'registration/multiuser_signup.html'
    return render(request, template_name=template_name)


def vendor_signup(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            messages.success(request, 'Successfully Signed as Vendor. Please Login to continue')
            #login(request, user)
            return redirect('login')
    else:
        context = {
        'form' : VendorForm(),
        'user_type' : 'Vendor'
        }
    return render(request, 'registration/signup.html', context)

def customer_signup(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            messages.success(request, 'Successfully Signed as Customer. Please Login to continue')
            #login(request, user)
            return redirect('login')
    else:
        form = VendorForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def view_profile(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        return render (request,'services/view_profile.html')

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UpdateProfile(request.POST, instance=request.user)
        if form.is_valid():
            update = form.save(commit=False)
            update.user = request.user
            update.save()
            messages.success(request, 'Your profile was updated successfully !')
            return redirect('view_profile')
        else:
            messages.error(request, 'Please fill details correctly.')
            return redirect('update_profile')
    else:
        form = UpdateProfile(instance=request.user)
        return render (request,'services/update_profile.html',{'form': form})
        
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            #return HttpResponse("Password updated successfully")
            return redirect('view_profile')
        else:
            messages.error(request, 'Please correct the error below.')
            return redirect('change_password')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })


def services(request):
    service_list = Service.objects.all().order_by("service_charge")
    paginator = Paginator(service_list, 6)
    page = request.GET.get('page')
    service = paginator.get_page(page)
    count = paginator.get_page(page)
    context = {
        'service' : service,
        'count' : count,
    }
    return render (request, 'services/services.html', context)

def service_info(request, id, service_name):
    service_name = service_name
    subservice = SubService.objects.filter(service=id).select_related()
    #total_subservice = SubService.objects.filter(service=id).select_related().count()
    paginator = Paginator(subservice, 6)
    page = request.GET.get('page')
    sub_service = paginator.get_page(page)
    count = paginator.get_page(page)
    context = {
        'subservice' : subservice,
        'service_name' : service_name,
        'sub_service' : sub_service,
        'count' : count,
        #'total_subservice' : total_subservice,
    }
    return render(request, 'services/filter.html', context)

# def vendors(request, id, service_name, service, sub_service_name):
#     cursor = connection.cursor()
#     cursor.execute("SELECT first_name, last_name, email, phone, service_name, sub_service_name, sub_service_charge from vendor_service join sub_service on vendor_service.sub_service = sub_service.id join service on sub_service.service = service.id join vendor on vendor_service.vendor = vendor.id join user on vendor.vendor = user.id")
#     row = cursor.fetchone()
#     sub_service_name = sub_service_name
#     #vendor = VendorService.objects.filter(sub_service=service).prefetch_related('sub_service','service','vendor').Vendor.objects.filter(vendor=id).select_related()
#     #total_subservice = SubService.objects.filter(service=id).select_related().count()
#     paginator = Paginator(row, 6)
#     page = request.GET.get('page')
#     vendor_detail = paginator.get_page(page)
#     count = paginator.get_page(page)
#     context = {
#         'vendor_detail' : vendor_detail,
#         'sub_service_name' : sub_service_name,
#         #'sub_service' : sub_service,
#         'count' : count,
#         #'total_subservice' : total_subservice,
#     }
#     return render(request, 'services/vendorservice.html', context)

# def service_detail(request):
#     service = Service.objects.get(id=id)
#     context = {
#         'service' : service,
#     }
#     return render(request, 'mastrooms/filter.html', context)

def deactivate_account(request):
    return render (request, 'services/index.html')

