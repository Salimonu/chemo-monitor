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
            biodata.patient = request.user
            biodata.save()
            return redirect('dashboards:index')
    
    # display a new form or invalid form
    return render(request, 'patients/biodata.html', {'form': form})
