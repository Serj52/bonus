from django import forms
from .models import Account, Trasaction

from django.core.exceptions import ValidationError


class AccountForm(forms.ModelForm):

    class Meta:
        error_css_class = 'error'
        model = Account
        fields = ['name', 'surname', 'tel_number', 'card_number', 'balance']
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Введите имя', 'class': 'form-control'}),
                   'surname': forms.TextInput(attrs={'placeholder': 'Введите фамилию', 'class': 'form-control'}),
                   'tel_number': forms.NumberInput(attrs={'placeholder': 'Введите тел.номер', 'class': 'form-control'}),
                   'card_number': forms.NumberInput(attrs={'placeholder': 'Введите номер карты', 'class': 'form-control'}),
                   'balance': forms.NumberInput(attrs={'placeholder': 'Введите баланс', 'class': 'form-control'}),
                   }

    def clean_tel_number(self):

        tel_number = str(self.cleaned_data['tel_number'])
        if len(tel_number) != 10:
            raise ValidationError('Проверьте число символов: {}'.format(len(tel_number)))
        return tel_number


