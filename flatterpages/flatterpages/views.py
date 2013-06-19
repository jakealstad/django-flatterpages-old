from django.shortcuts import render

from flatterpages.forms import PageForm
from flatterpages.models import Page, PageMedia, PageTemplate


def create_page(request):
	if request.method == 'POST':
		form = PageForm(request.POST)
		if form.is_valid():

			return derp

	else:
		form = PageForm()

	return render(request, 'base.html', {
		'form': form,
		})