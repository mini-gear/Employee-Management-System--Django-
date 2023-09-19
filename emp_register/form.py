from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import EmpRegister

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label='',max_length='20', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Fisrt Name'}))
    last_name = forms.CharField(label='',max_length='20', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    
    class meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	

designations = [('','Please Slect a Designation'),('Director','Director'),('Graphic Designer','Graphic Designer'),('Engineer','Engineer'),('Supervisor','Supervisor'),('Team Leader','Team Leader'),('Trainer','Trainer' ),('Co-Trainer','Co-Trainer'),('Intern','Intern'),('Sales Representative','Sales Representative')]

class AddEmployeeForm(forms.ModelForm):
    
    id = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'id', 'class':"form-control"}),label='')
    name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Name', 'class':"form-control"}), label='')
    designation = forms.CharField(required=True, widget=forms.widgets.Select(choices=designations, attrs={'placeholder':'Designation', 'class':"form-control"}), label='')
    salary = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Salary', 'class':"form-control"}), label='')
    mob_no = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Contact No', 'class':"form-control"}), label='')

    class Meta:
        model = EmpRegister
        exclude = ("user",)

class UpdateEmployeeForm(forms.ModelForm):
    id = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'id', 'class':"form-control"}),label='',disabled=True)
    name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Name', 'class':"form-control"}), label='')
    designation = forms.CharField(required=True, widget=forms.widgets.Select(choices=designations, attrs={'placeholder':'Designation', 'class':"form-control"}), label='')
    salary = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Salary', 'class':"form-control"}), label='')
    mob_no = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Contact No', 'class':"form-control"}), label='')

    class Meta:
        model = EmpRegister
        exclude = ("user",)

