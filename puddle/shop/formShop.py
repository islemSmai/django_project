from django import forms
from .models import Shop
INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'
class NewShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ('name','titre','logo','description','image','address','color','color_secondary')
        widgets = {
        'name':forms.TextInput(attrs={
            'class':INPUT_CLASSES,
        }),
        'titre':forms.TextInput(attrs={
            'class':INPUT_CLASSES,
        })
        ,
        'logo':forms.FileInput(attrs={
            'class':INPUT_CLASSES,
        }),
        'description':forms.Textarea(attrs={
            'class':INPUT_CLASSES,
        }),
        'image':forms.FileInput(attrs={
            'class':INPUT_CLASSES,
        }),
        'address':forms.TextInput(attrs={
            'class':INPUT_CLASSES,
        }),
        'color':forms.TextInput(attrs={
            'class':INPUT_CLASSES,
            'type': 'color',
            'id':"color",
            'value':"#ff0000"
        }),
        'color_secondary':forms.TextInput(attrs={
            'class':INPUT_CLASSES,
            'type': 'color',
            'id':"color_secondary",
            'value':"#ff0000"
        })
        }
class EditShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ('name','titre','logo','description','image','address','color','color_secondary')
        widgets = {
        'name':forms.TextInput(attrs={
            'class':INPUT_CLASSES,
        }),
        'titre':forms.TextInput(attrs={
            'class':INPUT_CLASSES,
        })
        ,
        'logo':forms.FileInput(attrs={
            'class':INPUT_CLASSES,
        }),
        'description':forms.Textarea(attrs={
            'class':INPUT_CLASSES,
        }),
        'image':forms.FileInput(attrs={
            'class':INPUT_CLASSES,
        }),
        'address':forms.TextInput(attrs={
            'class':INPUT_CLASSES,
        }),
       'color':forms.TextInput(attrs={
            'class':INPUT_CLASSES,
            'type': 'color',
            'id':"color",
            'value':"#ff0000"
        }),
        'color_secondary':forms.TextInput(attrs={
            'class':INPUT_CLASSES,
            'type': 'color',
            'id':"color_secondary",
            'value':"#ff0000"
        })
        }