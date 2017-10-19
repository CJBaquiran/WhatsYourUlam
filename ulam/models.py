from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Food(models.Model):
	food_name = models.CharField(max_length=140)
	food_caption = models.CharField(max_length=500)
	food_picture = models.FileField()

	def get_absolute_url(self):
		return reverse('ulam:detail', kwargs={'pk':self.pk})

	def __str__(self):
		return self.food_name + ' - ' + self.food_caption