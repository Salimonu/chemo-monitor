from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

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
            return redirect('patients:biodata')

    return render(request, 'core/signup.html', {'form': form})


@login_required
def login_redirect(request):
    user = request.user

    #PATIENT-CLINICIAN FLOW.
    # check if user is a patient and a verified clinician.
    if user.role == "patient" and user.is_verified_clinician:
        return render(request, 'core/select_role.html')

    # PATIENT FLOW.
    # check if user is a patient.
    if user.role == "patient":
        
        # check if user has not filled biodata
        patient = getattr(user, "patient", None)

        if not patient or not patient.is_complete:
            return redirect('patients:biodata')
        return redirect('patients:dashboard')

    
    # CLINICIAN FLOW.
    # check if user is a clinician.
    elif user.role == "clinician":        
        
        clinician = getattr(user, "clinician", None)
        
        #check if clinician has not filled biodata.
        if not clinician or not clinician.is_complete:
            return redirect('clinicians:biodata')
        
        #check if clinician has not submitted verification request.
        if not user.verification_requested:
            return redirect('clinicians:verification')
        
        #check if clinician has submitted verification request but not verified yet.
        if not user.is_verified_clinician:
        # if not clinician or not clinician.is_verified:
            
            #display verification request submitted succesfully.
            return redirect('clinicians:verification_review')
                
        return redirect('clinicians:dashboard')

    return redirect('core:index')
