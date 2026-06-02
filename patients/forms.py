from django import forms

from .models import Patient


class PatientBioDataForm(forms.ModelForm):
    class Meta:
        model= Patient
        fields = ('hospital_id', 'surname', 'first_name', 'middle_name', 'profile_picture', 'phone_number', 'emergency_contact', 'home_address', 'date_of_birth', 'gender', 'weight', 'height', 'next_of_kin_name', 'next_of_kin_relationship', 'blood_group')
