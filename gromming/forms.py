from django import forms
from .models import CustomizePackage, ServiceType

class CustomizePackageForm(forms.ModelForm):
    services = forms.ModelMultipleChoiceField(
        queryset=ServiceType.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = CustomizePackage
        fields = [
            'fullname',
            'phonenumber',
            'email',
            'address',
            # pet details
            'pet_name',
            'pet_type',
            'pet_breed',
            'pet_age',
            'pet_gender',
            'pet_weight',
            'pet_height',
            'pet_medical_condition',
            'pet_vaccination_status',
            'booking_date',
            'booking_time',
            'package_type',
            'services',
            'pet_image',
        ]
        widgets = {
            'booking_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control', 
            }),
            'booking_time': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control',
            }),
        }
