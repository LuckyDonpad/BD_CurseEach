from django import forms
from website.models import *


class LoginUserForm(forms.Form):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={"class": "form-input"}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-input"}))


class AddClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = '__all__'


class AddTasksForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ["name", "status", "end_date", "worker_id", ]


class AddWorkerForm(forms.ModelForm):
    class Meta:
        model = Workers
        fields = '__all__'


class ChangeWorkerForm(forms.ModelForm):
    class Meta:
        model = Workers
        fields = '__all__'


class ChangeClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = '__all__'


class ChangeTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'
