from django.db import models
from django.contrib.gis.db import models
from django.urls import reverse

# Create your models here.

GREEN_ROOF_TYPES = (
	(1, 'intensywny'),
    (2, 'półintensywny'),
    (3, 'ekstensywny'),
    (4, 'biosolarny'),
	)
    

ACCESSABILITY = (
	(1, 'tak'),
	(2, 'nie'),
)

OWNERSHIP = (
	(1, 'private'),
	(2, 'public'),
)


class Wola(models.Model):
    roof_type = models.IntegerField(choices=GREEN_ROOF_TYPES, verbose_name='Typ zielonego dachu: ')
    name = models.CharField(max_length=128)
    roof_address = models.CharField(max_length=256)
    area = models.IntegerField()
    total_place_area = models.IntegerField()
    access = models.IntegerField(choices=ACCESSABILITY, verbose_name='Dostępność: ')
    ownership_type = models.IntegerField(choices=OWNERSHIP, verbose_name='Rodzaj budynku: ')
   
    lon = models.FloatField()
    lat = models.FloatField()

    class Meta:
    	verbose_name='Wola'

    def __str__(self):
        return self.roof_address, self.roof_type

    def get_absolute_url(self):
        return reverse('wola', kwargs={'pk' : self.id})

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()