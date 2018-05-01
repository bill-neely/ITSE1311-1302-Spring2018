from django.contrib import admin

from .models import Zoo, Exhibit, Animal, ExhibitNeighbor

# Register your models here.


class ZooAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'logoFileName', 'get_absolute_url')

admin.site.register(Zoo, ZooAdmin)

class ExhibitAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'get_absolute_url')

admin.site.register(Exhibit, ExhibitAdmin)

class AnimalAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'exhibit', 'get_absolute_url', 'imageFileName')

admin.site.register(Animal, AnimalAdmin)

class ExhibitNeighborAdmin(admin.ModelAdmin):
	list_display = ('id', 'fromExhibit', 'direction', 'toExhibit')

admin.site.register(ExhibitNeighbor, ExhibitNeighborAdmin)
