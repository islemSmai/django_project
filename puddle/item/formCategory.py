from django import forms
from .models import Category
INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border '
class NewCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name','image')
        widgets = {
        'name':forms.TextInput(attrs={
            'class':INPUT_CLASSES,
            'style':'color:black'
        }),
        'image':forms.FileInput(attrs={
            'class':INPUT_CLASSES,
        })
        
        }
class EditCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name','image')
        widgets = {
        'name':forms.TextInput(attrs={
            'class':INPUT_CLASSES,
        }),
        'image':forms.FileInput(attrs={
            'class':INPUT_CLASSES,
        })}