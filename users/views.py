from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from home import urls
#from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.


@login_required
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! Youare now able to log in.')
            return redirect('register')
    else:        
        form = UserRegisterForm()
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)
    
@login_required
def profile(request):
    
    u_form = UserUpdateForm(instance=request.user)
    print("U_FORM")

    print(u_form)
    print("P_FORM")

    p_form = ProfileUpdateForm(instance=request.user)
    print(p_form)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

@login_required
def profileUpdate(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/updateprofile.html', context)


