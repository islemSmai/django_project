from django import forms

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class ContactForm(forms.Form):
    useremail = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': INPUT_CLASSES})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': INPUT_CLASSES})
    )
