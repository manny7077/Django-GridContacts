from django import forms
from .models import User

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'title',
            'first_name',
            'middle_name',
            'last_name',
            'job_title',
            'department',
            'office_location',
            'room_number',
            'plc_number',
            'personal_number',
            'status',
        ]
    title = forms.ChoiceField(choices=User.TITLE_CHOICES)
    status = forms.ChoiceField(choices=User.STATUS_CHOICES)


