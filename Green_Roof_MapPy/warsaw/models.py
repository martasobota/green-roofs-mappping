from django.contrib.gis.geos import GEOSGeometry
from django.db.models.fields import Field
from django.urls import reverse
from django.db import models
from django.contrib.gis.db import models
from django_google_maps import fields as map_fields



DISTRICTS = (
	(1, 'Wola'),
	(2, 'Śródmieście'),
	(3, 'Mokotów')
	)

GREEN_ROOF_TYPES = (
	(1, 'intensive'),
    (2, 'semi-intensive'),
    (3, 'extensive'),
    (4, 'biosolar'),
	)
    
ACCESSABILITY = (
	(1, 'yes'),
	(2, 'no'),
)


OWNERSHIP = (
	(1, 'private'),
	(2, 'public'),
)


class City(models.Model):
	name = models.CharField(max_length=128)

	def __str__(self):
		return "City: ".format(self.name)

#Class with name of the district in specific city
class District(models.Model):
	name = models.CharField(max_length=256)
	city = models.ForeignKey(City) #+ on_delete=models.CASCADE???

	def __str__(self):
		return format(self.name)

class GreenRoof(models.Model):
    district = models.ForeignKey(District) #+ on_delete=models.CASCADE???
    roof_address = models.CharField(max_length=256)
    roof_type = models.IntegerField(choices=GREEN_ROOF_TYPES, verbose_name='Green roof type')
    area = models.FloatField()
    total_place_area = models.FloatField()
    access = models.IntegerField(choices=ACCESSABILITY, verbose_name='Accessability')
    ownership_type = models.IntegerField(choices=OWNERSHIP, verbose_name='Type of the building')
    additional_info = models.CharField(max_length=1024, null=True)
    point = models.PointField(null=True, blank=True, verbose_name='Pin the place or search by address')
    # GeoManager is a must to make Geo Queries in Django
    objects = models.GeoManager()
    poly = models.PolygonField(null=True, blank=True, verbose_name='Pin the green roof area to create a polygon')
    objects = models.GeoManager()

    class Meta:
    	verbose_name='Green roof'
    	verbose_name_plural='Green roofs'

    def __str__(self):
        return "Green roof address: {}, district: {}, type: {}, area: {} sq m, total building's green roofs area: {}".format(self.roof_address, self.district, self.get_roof_type_display(), self.area, self.total_place_area)

    def get_absolute_url(self):
        return reverse('result-gr', kwargs={'pk' : self.id})
