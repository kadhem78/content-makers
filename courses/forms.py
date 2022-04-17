from  .models import Course
from django.forms import ModelForm
from django import forms


class CourseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categorie'].widget.attrs.update({'class': 'form-control'} )
        self.fields['title'].widget.attrs.update({'class': 'form-control' , 'placeholder' : 'course title'})
        self.fields['decription'].widget.attrs.update({'class': 'form-control' , 'placeholder' : 'course description'})
        self.fields['course_url'].widget.attrs.update({'class': 'form-control' , 'placeholder' : 'course link'})
        self.fields['level'].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = Course
        fields = ['categorie' , 'title' , 'course_img' , 'decription' , 'course_url' , 'level']


class SearchForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['keyword'].widget.attrs.update({'class': 'form-control'} )
    keyword = forms.CharField(max_length=50)

