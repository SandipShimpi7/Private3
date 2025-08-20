from django.db import models

class Slideshow(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(blank=True)

class SlideImage(models.Model):
	slideshow = models.ForeignKey(Slideshow, related_name='images', on_delete=models.CASCADE)
	image = models.ImageField(upload_to='slideshows/', blank=True, null=True)
	caption = models.CharField(max_length=200, blank=True)
