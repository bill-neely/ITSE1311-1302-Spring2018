from django.db import models
from django.urls import reverse

# Create your models here.

class Zoo(models.Model):
	name = models.CharField(max_length=200, help_text="Enter Zoo Name")
	logoFileName = models.CharField(max_length=200, help_text="Enter logo file name", null=True)

	def __str__ (self):
		return self.name

	def get_absolute_url(self):
		return reverse('zooDetail', args=[str(self.id)])

class Exhibit(models.Model):
	name = models.CharField(max_length=200, help_text="Enter Exhbit Name")
	zoo = models.ForeignKey('Zoo', on_delete=models.SET_NULL, null=True)

	def __str__ (self):
		return self.name

	def get_absolute_url(self):
		return reverse('exhibitDetail', args=[str(self.id)])

	def getNumberOfAnimals(self):
		return Animal.objects.filter(exhibit = self.id).count()

	def getZooName(self):
		return self.zoo.name

class ExhibitNeighbor(models.Model):
	fromExhibit = models.ForeignKey('Exhibit', on_delete=models.SET_NULL, null=True, related_name='fromExhibit')
	DIRECTIONS = (
		('n', 'North'),
		('s', 'South'),
		('e', 'East'),
		('w', 'West'),
		('nw', 'Northwest'),
		('sw', 'Southwest'),
		('ne', 'Northeast'),
		('se', 'Southeast'),
	)
	direction = models.CharField(max_length=2, choices=DIRECTIONS, help_text="Enter cardinal travel direction.")
	toExhibit = models.ForeignKey('Exhibit', on_delete=models.SET_NULL, null=True, related_name='toExhibit')

	def __str__(self):
		return str(self.id)

class Animal(models.Model):
	name = models.CharField(max_length=200, help_text="Enter Exhbit Name")
	imageFileName = models.CharField(max_length=200, help_text="Enter logo file name", null=True)
	exhibit = models.ForeignKey('Exhibit', on_delete=models.SET_NULL, null=True)
	soundFileName = models.CharField(max_length=200, help_text="Enter sound file name", null=True, blank=True)
	habitatDescription = models.TextField(max_length=1000, help_text='Enter a description of the habitat')
	dietDescription = models.TextField(max_length=1000, help_text='Enter a description of the diet')

	def __str__ (self):
		return self.name

	def get_absolute_url(self):
		return reverse('animalDetail', args=[str(self.id)])
