from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import Student, User , Location


class StudentSignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control' , 'placeholder' : 'username'} )
        self.fields['first_name'].widget.attrs.update({'class': 'form-control' , 'placeholder' : 'First name'} )
        self.fields['last_name'].widget.attrs.update({'class': 'form-control' , 'placeholder' : 'Last name'} )
        self.fields['email'].widget.attrs.update({'class': 'form-control' , 'placeholder' : 'Your Email'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control' , 'placeholder' : 'your password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control' , 'placeholder' : 're-write your password'})
        self.fields['domain'].widget.attrs.update({'class': 'form-control' , 'placeholder' : 'Domain of your content'})
        self.fields['location'].widget.attrs.update({'class': 'form-control'})
        self.fields['image_p'].widget.attrs.update({'value': 'Profile image'})
    """interests = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )"""
    location = forms.ModelChoiceField(queryset= Location.objects.all())
    image_p = forms.ImageField()
    domain = forms.CharField(max_length=70)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name' , 'last_name' , 'email', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.location = self.cleaned_data.get('location')
        user.save()
        domain = self.cleaned_data.get('domain')
        image_p = self.cleaned_data.get('image_p')
        student = Student.objects.create(user=user , domain = domain , profile_image = image_p)
        """student.interests.add(*self.cleaned_data.get('interests'))"""
        return user

class StudentCreation(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].widget.attrs.update({'class': 'form-control'} )
        self.fields['domain'].widget.attrs.update({'class': 'form-control'})
        self.fields['level'].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = Student
        fields = '__all__'


class UserFormAdmin(UserCreationForm):
    class Meta:
        model = User
        fields = "__all__"