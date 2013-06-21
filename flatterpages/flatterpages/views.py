from django.shortcuts import get_object_or_404, render
from django.template import Context, Template

from flatterpages.forms import PageForm
from flatterpages.models import Page, PageMedia, PageTemplate


def create_page(request):
	if request.method == 'POST':
		form = PageForm(request.POST)
		if form.is_valid():
			form.save()

	else:
		form = PageForm()

	return render(request, 'flatterpages_edit.html', {
		'form': form,
		})


def edit_page(request, slug):
	instance = get_object_or_404(Page, slug=slug)
	form = PageForm(request.POST or None, instance=instance)
	if form.is_valid():
		form.save()
	
	return render(request, 'flatterpages_edit.html', {
		'form': form,
		})


def render_page(request, slug):
	page = get_object_or_404(Page, slug=slug)

	return render(request, 'base.html', {
		'page': page,
		})

