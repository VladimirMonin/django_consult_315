from django import forms


class VisitForm(forms.Form):
    # Классы form-control, placeholder
    name = forms.CharField(label='Имя', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Имя', 'class': 'form-control'}))
    phone = forms.CharField(label='Телефон', max_length=20, widget=forms.TextInput(attrs={'type': 'tel', 'placeholder': 'Номер телефона', 'class': 'form-control'}))
    comment = forms.CharField(label='Комментарий', required=False, widget=forms.Textarea(attrs={'placeholder': 'Комментарий', 'class': 'form-control'}))