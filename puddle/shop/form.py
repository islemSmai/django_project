from django import forms
from .models import AboutUs
INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'
class NewAboutUsForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = ('description','gallery')
        widgets = {
        'description':forms.Textarea(attrs={
            'class':INPUT_CLASSES,
        }),
        'gallery':forms.FileInput(attrs={
            'class':INPUT_CLASSES,
        }),
        }
class EditAboutUsForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = ('description','gallery')
        widgets = {
        'description':forms.Textarea(attrs={
            'class':INPUT_CLASSES,
        }),
        'gallery':forms.FileInput(attrs={
            'class':INPUT_CLASSES,
        })
        }