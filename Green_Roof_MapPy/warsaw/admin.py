# from django.contrib import admin
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