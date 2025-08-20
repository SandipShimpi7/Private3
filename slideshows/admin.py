from django.contrib import admin
from .models import Slideshow, SlideImage

class SlideImageInline(admin.TabularInline):
	model = SlideImage
	extra = 1

@admin.register(Slideshow)
class SlideshowAdmin(admin.ModelAdmin):
	inlines = [SlideImageInline]
	list_display = ('title',)

@admin.register(SlideImage)
class SlideImageAdmin(admin.ModelAdmin):
	list_display = ('slideshow', 'caption', 'image')
