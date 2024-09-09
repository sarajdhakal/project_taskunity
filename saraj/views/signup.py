from django.shortcuts import render, redirect
from ..forms import SignUpForm
from django.contrib import messages

def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = SignUpForm()

        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, f'Account created for {form.cleaned_data["username"]}')
                return redirect('signup')

    return render(request, 'signup.html', {'form': form})