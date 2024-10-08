from django.shortcuts import render, redirect
from ..forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def signup(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account created for {form.cleaned_data["username"]}')
            return redirect('signup')

    return render(request, 'signup.html', {'form': form})
