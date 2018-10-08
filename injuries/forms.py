from django import forms
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Field, Div

from .models import Injury


class InjuryForm(forms.ModelForm):

    class Meta:
        model = Injury
        fields = '__all__'
        widgets = {
            'date_of_injury': forms.DateInput(attrs={'type': 'date'}),
            'date_of_return': forms.DateInput(attrs={'type': 'date'})
        }

    helper = FormHelper()
    helper.form_tag = False
    helper.layout = Layout(
        Div('athlete', css_class='col-md-6'),
        Div('date_of_injury', css_class='col-md-6'),
        Div('date_of_return', css_class='col-md-6'),
        Div('participation', css_class='col-md-6'),
        Div('injured_body_part', css_class='col-md-6'),
        Div('left_right', css_class='col-md-6'),
        Div('type_of_injury', css_class='col-md-6'),
        Div('where_it_happened', css_class='col-md-6'),
        Div('cause_of_injury', css_class='col-md-6'),
        Div('contact_collision', css_class='col-md-6'),
        Div('mechanism', css_class='col-md-6'),
        Div('place_of_injury', css_class='col-md-6'),
    )


