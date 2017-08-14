from django import forms


# our new form


class ContactForm(forms.Form):
    FirstName = forms.CharField(required=True)
    LastName = forms.CharField(required=True)
    Email = forms.EmailField(required=True)



