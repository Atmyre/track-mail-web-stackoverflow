from django.shortcuts import redirect, render
from django.contrib import auth
from .forms import UserForm, UserProfileForm
from django.template import RequestContext
import sys

def login(request, next):
    print next

    authenticated = False
    redirect_to = next
    login_error = None

    if request.method == 'POST':

        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            authenticated = True
        else:
            login_error = "User not found"

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    if authenticated:
        auth.login(request, user)
        return redirect(redirect_to)
    else:
        return render(request, 'login/login.html', {'login_error': login_error, 'user_form': UserForm(), \
                                                 'user_profile_form': UserProfileForm(), 'redirect_to' : redirect_to})

def logout(request, next):
    auth.logout(request)
    redirect_to = next
    return redirect(redirect_to)  


def register(request, next):
    context = RequestContext(request)
    registered = False

    if request.method == 'POST':
       
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            sys.stdout.flush()

            profile.save()

            registered = True

        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    

    redirect_to = next
    if registered == False:
        return render(request, 'login/register.html', {'user_form': user_form, 'user_profile_form': profile_form, 'redirect_to' : redirect_to})
    else:
        return redirect(redirect_to)
    
