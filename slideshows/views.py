from django.shortcuts import render, get_object_or_404
from .models import Slideshow

def slideshow_list(request):
	slideshows = Slideshow.objects.all()
	return render(request, 'slideshows/slideshow_list.html', {'slideshows': slideshows})

def slideshow_detail(request, pk):
	slideshow = get_object_or_404(Slideshow, pk=pk)
	return render(request, 'slideshows/slideshow_detail.html', {'slideshow': slideshow})
