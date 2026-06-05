from django.shortcuts import render, redirect
from .forms import ClinicianVerificationForm, ClinicianBioDataForm


def create_clinician_biodata(data):
    # create a form with the submitted data
    form = ClinicianBioDataForm(data.POST, data.FILES)
    if form.is_valid():
        biodata = form.save(commit=False)
        biodata.user = data.user
        biodata.is_complete = True
        biodata.save()
        return None
    return form
        

def verify_clinician(data):
    user = data.user
    #load the verification form with text and image.
    form = ClinicianVerificationForm(data.POST, data.FILES)
    if form.is_valid():
        verification_form = form.save(commit=False)
        verification_form.user = user
        verification_form.save()
        
        # Get clinician relation related to user
        # clinician = getattr(user, "clinician", None)
        
        #change the verification request status.
        user.verification_requested = True
        user.save()

        return None
    return form
     