from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import PatientBioDataForm


@login_required
def biodata(request):
    
    if request.method != 'POST':    
        # create a new form
        form = PatientBioDataForm()
    
    else:
        # create a form with the submitted data
        form = PatientBioDataForm(request.POST, request.FILES)
        if form.is_valid():
            biodata = form.save(commit=False)
            biodata.user = request.user
            biodata.is_complete = True
            biodata.save()
            return redirect('patients:dashboard')
    
    # display a new form or invalid form
    return render(request, 'patients/biodata.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'patients/dashboard.html')


@login_required
def request_verification(request):
    pass
    # user = request.user

    # # Only patients can access this page.
    # if user.role != "patient":
    #     return redirect('core:login_redirect')
    
    # if request.method == 'POST':
    #     user.role = "clinician"
    #     user.save()
    
    #     return redirect("clinicians:verification")

    # return render(request, "clinicians/request_verification.html")
