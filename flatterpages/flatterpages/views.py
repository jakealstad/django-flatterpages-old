from django.shortcuts import get_object_or_404, render
from django.template import Context, Template

from flatterpages.forms import PageForm, PageTemplateForm, UserTemplateForm
from flatterpages.models import Page, PageMedia, PageTemplate, UserTemplate


def create_page(request):
	if request.method == 'POST':
		form = PageForm(request.POST)
		if form.is_valid():
			form.save()

	else:
		form = PageForm()

	return render(request, 'edit-page.html', {
		'form': form,
		})


def edit_page(request, slug):
	instance = get_object_or_404(Page, slug=slug)
	form = PageForm(request.POST or None, instance=instance)
	if form.is_valid():
		form.save()
	
	return render(request, 'edit-page.html', {
		'form': form,
		})


def render_page(request, slug):
	page = get_object_or_404(Page, slug=slug)

	return render(request, 'base.html', {
		'page': page,
		})


def manage_pages(request):
	pages = Page.objects.all()

	return render(request, 'manage-pages.html', {
		'pages': pages,
		})


def create_page_template(request):
	if request.method == 'POST':
		form = PageTemplateForm(request.POST)
		if form.is_valid():
			form.save()

	else:
		form = PageTemplateForm()

	return render(request, 'edit-template.html', {
		'form': form,
		})


def create_user_template(request):
	if request.method == 'POST':
		form = UserTemplateForm(request.POST)
		if form.is_valid():
			form.save()

	else:
		form = UserTemplateForm()

	return render(request, 'edit-template.html', {
		'form': form,
		})


def edit_page_template(request, slug):
	instance = get_object_or_404(PageTemplate, slug=slug)
	form = PageTemplateForm(request.POST or None, instance=instance)
	if form.is_valid():
		form.save()

	return render(request, 'edit-template.html', {
		'form': form,
		})


def edit_user_template(request, slug):
	instance = get_object_or_404(UserTemplate, slug=slug)
	form = UserTemplateForm(request.POST or None, instance=instance)
	if form.is_valid():
		form.save()

	return render(request, 'edit-template.html', {
		'form': form,
		})


def manage_templates(request):

	return render(request, 'manage-page-templates.html')