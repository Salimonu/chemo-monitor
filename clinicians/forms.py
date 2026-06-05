from django import forms

from .models import ClinicianVerification, Clinician


class ClinicianBioDataForm(forms.ModelForm):
    class Meta:
        model= Clinician
        fields = ('surname', 'first_name', 'middle_name', 'profile_picture', 'phone_number', 'email', 'gender', 'date_of_birth', 'specialty', 'bio')


class ClinicianVerificationForm(forms.ModelForm):
    class Meta:
        model= ClinicianVerification
        fields = ('hospital', 'registration_number', 'license_number', 'license_expiration_date', 'current_license')
        