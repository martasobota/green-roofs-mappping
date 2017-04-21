from django.contrib.gis import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.gis.geos import GEOSGeometry
from warsaw.models import *

# from django.db import models
# from django_google_maps import widgets as map_widgets
# from django_google_maps import fields as map_fields
# from warsaw.models import City, District, GreenRoof, Rental
# from mapwidgets.widgets import GooglePointFieldWidget
# from django.contrib.gis.db import models

# class RentalAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
#     }


# class CityAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.PointField: {"widget": GooglePointFieldWidget}
#     }

# class GreenRoofAdmin(admin.OSMGeoAdmin):
# 	list_display = ['district', 'roof_address', 'roof_type', 'area', 'total_place_area', 'access', 'ownership_type', 'point', 'additional_info']
# 	search_fields = ['roof_address', 'roof_type', 'ownership_type']

admin.site.register(GreenRoof, admin.OSMGeoAdmin)
