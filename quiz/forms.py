from django import forms
from .models import Participant
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'student_class', 'age', 'gender', 'institution']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'student_class': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'institution': forms.TextInput(attrs={'class': 'form-control'}),
        }
    

class UserRegistrationForm(UserCreationForm):

    student_class = forms.CharField(max_length=555, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                  'placeholder': 'This field is required'
                                                                                  }) )

    age = forms.IntegerField(widget=forms.NumberInput(attrs={ 'class': 'form-control',
                                                             'placeholder': 'This field is required'
                                                             }))

    gender = forms.ChoiceField(choices=Participant.GENDER_CHOICES,
        widget=forms.Select(attrs={ 'class': 'form-control'})
    )

    institution = forms.CharField(
        max_length=255, widget=forms.TextInput(attrs={ 'class': 'form-control'})
    )

    email = forms.EmailField( required=True, widget=forms.EmailInput(attrs={ 'class': 'form-control'}) )
    

    username = forms.CharField( widget=forms.TextInput(attrs={ 'class': 'form-control'}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control' }))
                                                                  
                                                                  

    password2 = forms.CharField( widget=forms.PasswordInput(attrs={ 
                                                                   'class': 'form-control',
                                                                   'placeholder': 'This field is required'
                                                                   }))

    class Meta:
        model = User
        fields = [ 'username', 'email', 'password1', 'password2',]


    

    
     
        
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ['username', 'password']
        


class cleanForm(forms.Form):
    def clean(self):
        cleaned_data = super().clean()
        for field in self.fields:
            value = cleaned_data.get(field)
            if isinstance(value, str):
                cleaned_data[field] = value.strip()
        return cleaned_data
    
    
class cleanUserForm(UserCreationForm):
    def clean(self):
        cleaned_data = super().clean()
        for field in self.fields:
            value = cleaned_data.get(field)
            if isinstance(value, str):
                cleaned_data[field] = value.strip()
        return cleaned_data
    
    
