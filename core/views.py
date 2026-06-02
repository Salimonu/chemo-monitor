from django.shortcuts import render, redirect

from .forms import SignUpForm


def index(request):
    return render(request, 'core/index.html')


def signup(request):
    if request.method != 'POST':
        form = SignUpForm()
    else:
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboards:index')

    return render(request, 'core/signup.html', {'form': form})
