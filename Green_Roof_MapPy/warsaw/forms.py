from django import forms 
from django.db.models import Value
from django.db.models.functions import Concat
from exercises.models import (
	City,
	District,
	GreenRoof,
	)

from exercises.validators import valid_range
from django.contrib.auth import authenticate

class AuthForm(forms.Form):
	login = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self):
		'''
		Metoda dorzuca do cleaned_data instancję użytkownika pod kluczem 'user'
		'''
		cleaned_data = super().clean()

		login = cleaned_data['login']
		password = cleaned_data['password']
		user=authenticate(username=login,password=password)
		if user is None:
			raise forms.ValidationError('Błędny login lub hasło')

		cleaned_data['user'] = user
		return cleaned_data