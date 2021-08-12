import random, hashlib

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

from users.models import User, ExtendUser

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите адрес эл. почты'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите фамилию'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите возраст'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name',  'age', 'password1', 'password2')

        # def save(self):
        #     user = super().save()
        #     user.is_active = False
        #     salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
        #     user.activation_key = hashlib.sha1((user.email + salt).encode('utf8')).hexdigest()
        #     user.save()
        #     return user


class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control py-4'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control py-4'}), required=False)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'image', 'age')

    # def __init__(self, *args, **kwargs):
    #     super(UserChangeForm, self).__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['class'] = 'form-control'
    #         field.help_text = ''
    #         if field_name == 'password':
    #             field.widget = forms.HiddenInput()

    # def clean_age(self):
    #     data = self.cleaned_data['age']
    #     if data < 18:
    #         raise forms.ValidationError("Вы слишком молоды!")
    #
    #     return data

class ExtendUserProfileForm(forms.ModelForm):
    # tagline = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    # about_me = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    # gender = forms.ChoiceField(choices=ExtendUser.GENDER_CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = ExtendUser
        fields = ('tagline', 'about_me', 'gender')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widgets.attrs['class'] = 'form-control py-4'
                field.help_texts = ''
                if field_name == 'about_me':
                    field.widget = forms.TextInput()
