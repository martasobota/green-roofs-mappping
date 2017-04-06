
from django.db.models import Value
from django.db.models.functions import Concat
from warsaw.models import (
	City,
	District,
	GreenRoof,
	ACCESSABILITY,
	GREEN_ROOF_TYPES,
	OWNERSHIP,
	)

from django.contrib.auth import authenticate
from django import forms 
from django.contrib.gis import forms
import floppyforms as forms
# import floppyforms.__future__ as forms



class AddGreenRoofForm(forms.Form):
	roof_address = forms.CharField(max_length=256)
	roof_type = forms.ChoiceField(choices=GREEN_ROOF_TYPES)
	area = forms.FloatField()
	total_place_area = forms.FloatField()
	access = forms.ChoiceField(choices=ACCESSABILITY)
	ownership_type = forms.ChoiceField(choices=OWNERSHIP)
	poly = forms.gis.PolygonField()
	additional_info = forms.CharField(required=False)


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


class SearchForm(forms.Form): 
	address = forms.CharField(label='Green Roof Address', max_length=100)


class GMapPolygonWidget(forms.gis.BaseGMapWidget, forms.gis.PolygonWidget):
    google_maps_api_key = 'AIzaSyBgFBEhKWM98zvpQHY1h2C_VaVqMDQ2urE'

class GmapForm(forms.Form):
    poly = forms.gis.PolygonField(widget=GMapPolygonWidget)

class Media:
    extend = False
    js = ('js/openlayers/OpenLayers.js',
          'https://maps.google.com/maps/api/js?v=3&sensor=false',
          'floppyforms/js/MapWidget.js')

