from django.forms import ModelForm, DateInput
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ('date', )