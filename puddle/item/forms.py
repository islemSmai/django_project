from django import forms
from .models import Item,Category
INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'
class NewItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        shop = kwargs.pop('shop', None)
        super().__init__(*args, **kwargs)
        if shop is not None:
            # Get distinct Category objects for the specific shop
            distinct_categories = Category.objects.filter(shop=shop).distinct()
            # Set the queryset for the category field to the distinct Category objects
            self.fields['category'].queryset = distinct_categories


        # Apply custom CSS classes to form fields
        self.fields['category'].widget.attrs.update({'class': INPUT_CLASSES})
        self.fields['name'].widget.attrs.update({'class': INPUT_CLASSES})
        self.fields['description'].widget.attrs.update({'class': INPUT_CLASSES})
        self.fields['price'].widget.attrs.update({'class': INPUT_CLASSES})
        self.fields['quantity'].widget.attrs.update({'class': INPUT_CLASSES})
        self.fields['image'].widget.attrs.update({'class': INPUT_CLASSES})

    class Meta:
        model = Item
        fields = ('category','name','description','price','quantity','image')
        widgets = {
        'category':forms.Select(attrs={
            'class':INPUT_CLASSES,
        }),
        'name':forms.TextInput(attrs={
            'class':INPUT_CLASSES,
        }),
        'description':forms.Textarea(attrs={
            'class':INPUT_CLASSES,
        }),
        'price':forms.TextInput(attrs={
            'class':INPUT_CLASSES,
        }),
        'quantity':forms.TextInput(attrs={
            'class':INPUT_CLASSES,
        }),
        'image':forms.FileInput(attrs={
            'class':INPUT_CLASSES,
        })
        
        }
        gallery = forms.FileField(
        widget=forms.FileInput(attrs={'allow_multiple_selected': True}),
        required=False)
class EditItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        shop = kwargs.pop('shop', None)
        super().__init__(*args, **kwargs)
        if shop is not None:
            # Get distinct Category objects for the specific shop
            distinct_categories = Category.objects.filter(shop=shop).distinct()
            # Set the queryset for the category field to the distinct Category objects
            self.fields['category'].queryset = distinct_categories


        # Apply custom CSS classes to form fields
        self.fields['category'].widget.attrs.update({'class': INPUT_CLASSES})
        self.fields['name'].widget.attrs.update({'class': INPUT_CLASSES})
        self.fields['description'].widget.attrs.update({'class': INPUT_CLASSES})
        self.fields['price'].widget.attrs.update({'class': INPUT_CLASSES})
        self.fields['quantity'].widget.attrs.update({'class': INPUT_CLASSES})
        self.fields['image'].widget.attrs.update({'class': INPUT_CLASSES})
    class Meta:
        model = Item
        fields = ('category','name','description','price','quantity','image','is_sold')
        widgets = {
        'category':forms.Select(attrs={
            'class':INPUT_CLASSES,
        }),
        'name':forms.TextInput(attrs={
            'class':INPUT_CLASSES,
        }),
        'description':forms.Textarea(attrs={
            'class':INPUT_CLASSES,
        }),
        'price':forms.TextInput(attrs={
            'class':INPUT_CLASSES,
        }),
         'quantity':forms.NumberInput(attrs={
            'class':INPUT_CLASSES,
        }),
        'image':forms.FileInput(attrs={
            'class':INPUT_CLASSES,
        })
        }
        gallery = forms.FileField(
        widget=forms.FileInput(attrs={'allow_multiple_selected': True}),
        required=False)