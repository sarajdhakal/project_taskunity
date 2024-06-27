from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect
from ..forms import UserLoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            form = UserLoginForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    print(user)
                    login(request, user)
                    return redirect('index')
                else:
                    messages.info(request, 'Username or Password is incorrect')
        else:
            form = UserLoginForm()
        return render(request, 'login.html', {'form': form})


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')
