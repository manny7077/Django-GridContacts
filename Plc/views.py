from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, redirect , get_object_or_404
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from .forms import EditProfileForm
from django.contrib import messages

#import your views here.
def is_management(user):
    return user.is_authenticated and user.is_management

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            if user.is_staff:
                messages.success(request, 'You have successfully logged in as staff.')
                return redirect('staff')
            elif user.is_management:
                messages.success(request, 'You have successfully logged in as management.')
                return redirect('management')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
    return render(request, 'login.html')



def staff_details_view(request):
    staffs = User.objects.filter(is_staff=True, is_superuser=False) | User.objects.filter(is_management=True, is_superuser=False)
    return render(request, 'staff_details.html', {'staffs': staffs})

@login_required
def staff_view(request):
    staffs = User.objects.filter(is_staff=True, is_superuser=False) | User.objects.filter(is_management=True, is_superuser=False)
    return render(request, 'staff.html', {'staffs': staffs})


@login_required
@user_passes_test(is_management, login_url='staff')
def management_view(request):
    staffs = User.objects.filter(is_staff=True, is_superuser=False) | User.objects.filter(is_management=True, is_superuser=False)
    return render(request, 'management.html',{'staffs':staffs})



def logout_view(request):
    auth_logout(request)
    return redirect('staff_details')  



@login_required
def edit_profile_form(request, staff_number):
    edit_user = get_object_or_404(User, staff_number=staff_number)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=edit_user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile has been successfully updated")
            return redirect('management') 
    else:
        form = EditProfileForm(instance=edit_user)

    return render(request, 'edit_profile_form.html', {'form': form, 'edit_user': edit_user})



@login_required
def edit_user(request, staff_number):
    user = get_object_or_404(User, staff_number=int(staff_number))

    if request.method == 'POST':
        if request.user == user or request.user.is_management:
            form = EditProfileForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, "Profile has been successfully updated")
                return redirect('management')
        else:
            messages.error(request, "You are not allowed to edit this profile.")
            return redirect('management')
    else:
        if request.user == user or request.user.is_management:
            form = EditProfileForm(instance=user)
        else:
            messages.error(request, "You are not allowed to view this profile.")
            return redirect('management')
    return render(request, 'edit_profile_form.html', {'form': form, 'edit_user': user})

