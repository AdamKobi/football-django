from django import forms
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Field, Div

from .models import Player


class PlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = '__all__'
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'})
        }

    helper = FormHelper()
    helper.form_tag = False
    helper.layout = Layout(
        Div('first_name', css_class='col-md-6'),
        Div('last_name', css_class='col-md-6'),
        Div('position', css_class='col-md-6'),
        Div('birth_date', css_class='col-md-6'),
        Div('weight', css_class='col-md-6'),
        Div('height', css_class='col-md-6'),
        Div('image', css_class='col-md-6'),
        Div('is_active', css_class='col-md-6'),
    )