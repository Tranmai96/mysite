from django import forms

from django.forms import ModelForm

from .models import Lesson

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'
        #go ahead and create all the field 
        #nếu chỉ muốn đăng ký vài field thì ghi là:
        # fields= ['student']


