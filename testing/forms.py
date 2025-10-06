from django import forms
from .models import Booking
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["room", "start_date","end_date"]
        widgets = {
            "start_date":forms.DateInput(attrs={"type":"date"}),
            "end_date": forms.DateInput(attrs={"type":"date"}),
        }
        
class CustomSignUpForm(UserCreationForm):
    username = forms.CharField(
        label='Логін',
        max_length=30,
        help_text='• Максимальна довжина: 30 символів.<br>• Лише латинські літери, цифри та @/./+/-/_<br>Буде використаний для входу в систему.<br>',
    )
    first_name = forms.CharField(
        label='Імя',
        max_length=30,
        help_text='• Максимальна довжина: 30 символів.<br>',
    )
    last_name = forms.CharField(
        label='Прізвище',
        max_length=30,
        help_text='• Максимальна довжина: 30 символів.<br>',
    )
    password1 = forms.CharField(
        label='Пароль',
        min_length=8,
        widget=forms.PasswordInput,
        help_text='• Мінімальна довжина: 8 символів. <br>• Ваш пароль не повинен бути занадто простим.<br>• Ваш пароль не повинен бути схожим на інші ваші особисті дані.<br>• Ваш пароль не повинен складатися лише з цифр.<br>',
    )
    password2 = forms.CharField(
        label='Підтвердження пароля',
        widget=forms.PasswordInput,
    )
    email = forms.EmailField(label='Email', max_length=100)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")
        
class CustomLogInForm(AuthenticationForm):
    username = forms.CharField(
        label='Логін',
        max_length=30,
        help_text='• Максимальна довжина: 30 символів.<br>• Лише латинські літери, цифри та @/./+/-/_<br>',
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput,
        help_text='• Мінімальна довжина: 8 символів.',
    )
    error_messages = {
        "invalid_login": "Невірний логін або пароль. Перевірте правильність введених даних.",
    }
    class Meta:
        model = User
        fields = ("username", "password")