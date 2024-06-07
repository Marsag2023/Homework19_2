from django.forms import ModelForm, forms

from catalog.models import Product, Version, Category
from django.forms.fields import BooleanField
forbidden_words = ['казино',
                   'криптовалюта',
                   'крипта',
                   'биржа',
                   'дешево',
                   'бесплатно',
                   'обман',
                   'полиция',
                   'радар']


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ("number_of_views", "owner")

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        for word in forbidden_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'Нельзя использовать слова: {forbidden_words} !!!')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        for word in forbidden_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'Нельзя использовать слова: {forbidden_words} !!!')
        return cleaned_data


class ProductModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ("category", "description", "publication")


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = "__all__"

    def clean_name(self):
        cleaned_data = self.cleaned_data['version_name']
        for word in forbidden_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'Нельзя использовать слова: {forbidden_words}')
        return cleaned_data




class CategoryForm(StyleFormMixin,ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
