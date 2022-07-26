from django import forms  # import forms from django
from .models import Item  # import our defined Item model

# new model that will inherit all the functions from django ModelForms
class ItemForm(forms.ModelForm):
    class Meta:  # an inner class that gives our form some self information
        model = Item
        fields = ['name', 'done']