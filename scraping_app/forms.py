from django import forms

from scraping_app.models import City, Language


# вывод форм
# https://docs.djangoproject.com/en/4.2/ref/forms/api/#outputting-forms-as-html
class FindForm(forms.Form):
    city = forms.ModelChoiceField(queryset=City.objects.all(),
                                  to_field_name='slug', required=False,
                                  widget=forms.Select(attrs={'class': 'form-control'}),
                                  label='Город')
    language = forms.ModelChoiceField(queryset=Language.objects.all(),
                                      to_field_name='slug', required=False,
                                      widget=forms.Select(attrs={'class': 'form-control'}),
                                      label='Язык')
