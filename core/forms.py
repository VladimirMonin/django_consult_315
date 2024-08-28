from django import forms
from .models import Visit


class VisitForm(forms.Form):
    # Классы form-control, placeholder
    name = forms.CharField(label='Имя', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Имя', 'class': 'form-control'}))
    phone = forms.CharField(label='Телефон', max_length=20, widget=forms.TextInput(attrs={'type': 'tel', 'placeholder': 'Номер телефона', 'class': 'form-control'}))
    comment = forms.CharField(label='Комментарий', required=False, widget=forms.Textarea(attrs={'placeholder': 'Комментарий', 'class': 'form-control'}))

    # Валидация данных данных происходит через расширение\переопределене методов
    # clean_<field_name> например, проверим что каждый элемент имени является строкой
    def clean_name(self):
        name = self.cleaned_data["name"]
        
        if not isinstance(name, str):
            # Поднимаем исключение, которое попадет в контекст шаблона
            raise forms.ValidationError("Имя должно быть строкой")
        return name


class VisitModelForm(forms.ModelForm):
    # Какие поля мы хотим видить?
    class Meta:
        model = Visit
        fields = ['name', 'phone', 'comment']
