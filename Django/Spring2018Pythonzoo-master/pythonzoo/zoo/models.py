from django.db import models

# Create your models here.

class Zoo(models.Model):
	name = models.CharField(max_length=200, help_text="Enter Zoo Name")
	
	def __str__ (self):
		return self.name

class Exhibit(models.Model):
	name = models.CharField(max_length=200, help_text="Enter Exhbit Name")
	zoo = models.ForeignKey('Zoo', on_delete=models.SET_NULL, null=True) 
	
