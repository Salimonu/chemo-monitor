from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import ClinicianVerificationForm, ClinicianBioDataForm

from .services import create_clinician_biodata, verify_clinician


@login_required
def biodata(request):
    
    if request.method != 'POST':    
        # create a new form
        form = ClinicianBioDataForm()
    
    else:
        # Create a clinician biodata
        form = create_clinician_biodata(request)

        if form is None:
            return redirect('clinicians:verification')

        # # create a form with the submitted data
        # form = ClinicianBioDataForm(request.POST, request.FILES)
        # if form.is_valid():
        #     biodata = form.save(commit=False)
        #     biodata.clinician = request.user
        #     biodata.is_complete = True
        #     biodata.save()
            # return redirect('clinicians:verification')
    
    # display a new form or invalid form
    return render(request, 'clinicians/biodata.html', {'form': form})


@login_required
def verification(request):
    user = request.user

    # PATIENT APPLIES FOR CLINICIAN VERIFICATION.
    if user.role == "patient" and not hasattr(user, "clinician"):
        return redirect('clinicians:biodata')

    # # Only clinicians can access this page.
    # if user.role != "clinician":
    #     return redirect('core:login_redirect')

    # Get clinician relation related to user
    # clinician = getattr(user, "clinician", None)
    
    # Already submitted request.
    if user.verification_requested:
        
        #verification request submitted succesfully.
        return redirect('clinicians:verification_review')
    
    # Already verified clinician.
    if user.is_verified_clinician:
        return redirect('clinicians:dashboard')
    
    # Handle form
    if request.method == 'POST':
        # Create verification request
        form = verify_clinician(request)
        
        if form is None:
            #verification request submitted succesfully.
            return redirect('clinicians:verification_review')
   

        # #load the verification form with text and image.
        # form = ClinicianVerificationForm(request.POST, request.FILES)
        # if form.is_valid():
        #     verification_form = form.save(commit=False)
        #     verification_form.clinician = request.user
        #     verification_form.save()
                
        #     #change the verification request status.
        #     request.user.verification_requested = True
        #     request.user.save()
                
        #     #verification request submitted succesfully.
        #     return redirect('clinicians:verification_review')
        
    else:
        #generate a new verication form.
        form = ClinicianVerificationForm()
     
    # display a new form or invalid form
    return render(request, 'clinicians/verification.html', {'form': form})


@login_required
def verification_review(request):
    user = request.user
    #Display a message that verification request was submitted successfully.
     
    # # Only clinicians can access this page.
    # if user.role != "clinician":
    #     return redirect('core:login_redirect')
    
    # Get clinician relation related to user
    # clinician = getattr(user, "clinician", None)

    #check if clinician has not submitted verification request.
    if not user.verification_requested:
        return redirect('clinicians:verification')
    
    else:
        return render(request, 'clinicians/verification_review.html')


@login_required
def dashboard(request):
    return render(request, 'clinicians/dashboard.html')

