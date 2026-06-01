from django.shortcuts import render

from .forms import SignUpForm


def signup(request):
    form = SignUpForm()

    return render(request, 'core/signup.html')
