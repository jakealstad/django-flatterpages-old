import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.template import Context, Template

from flatterpages.forms import PageForm, PageTemplateForm, UserTemplateForm, StylesheetForm
from flatterpages.models import Page, PageMedia, PageTemplate, UserTemplate, Stylesheet


@login_required
def create_page(request):
	if request.method == 'POST':
		form = PageForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = PageForm()

	user_templates = UserTemplate.objects.filter(user=request.user)

	return render(request, 'edit-page.html', {
		'form': form,
		'user_templates': user_templates,
		})


@login_required
def edit_page(request, url):
	instance = get_object_or_404(Page, url=url)
	form = PageForm(request.POST or None, instance=instance)
	if form.is_valid():
		form.save()
	
	user_templates = UserTemplate.objects.filter(user=request.user)

	return render(request, 'edit-page.html', {
		'form': form,
		'user_templates': user_templates,
		})


def render_page(request, url):
	page = get_object_or_404(Page, url=url)

	if page.parent_page:
		print str(page.parent_page) + '>' + str(page)

	return render(request, 'base.html', {
		'page': page,
		})


@login_required
def manage_pages(request):
	pages = Page.objects.all()

	return render(request, 'manage-pages.html', {
		'pages': pages,
		})


@login_required
def delete_page(request, url):
	page = get_object_or_404(Page, url=url)
	page.delete()

	return redirect(manage_pages)


@login_required
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


@login_required
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


@login_required
def edit_page_template(request, id):
	instance = get_object_or_404(PageTemplate, id=id)
	form = PageTemplateForm(request.POST or None, instance=instance)
	if form.is_valid():
		form.save()

	return render(request, 'edit-template.html', {
		'form': form,
		})


@login_required
def edit_user_template(request, id):
	instance = get_object_or_404(UserTemplate, id=id)
	form = UserTemplateForm(request.POST or None, instance=instance)
	if form.is_valid():
		form.save()

	return render(request, 'edit-template.html', {
		'form': form,
		})


@login_required
def manage_page_templates(request):
	templates = PageTemplate.objects.all()

	return render(request, 'manage-page-templates.html', {
		'templates': templates,
		})


@login_required
def manage_user_templates(request):
	templates = UserTemplate.objects.all()

	return render(request, 'manage-user-templates.html', {
		'templates': templates,
		})


@login_required
def delete_page_template(request, id):
	instance = get_object_or_404(PageTemplate, id=id)
	instance.delete()

	return redirect(manage_page_templates)


@login_required
def delete_user_template(request, id):
	instance = get_object_or_404(UserTemplate, id=id)
	instance.delete()

	return redirect(manage_user_templates)


@login_required
def create_stylesheet(request):
	if request.method == 'POST':
		form = StylesheetForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = StylesheetForm()

	return render(request, 'edit-stylesheet.html', {
		'form': form,
		})


@login_required
def edit_stylesheet(request, id):
	instance = get_object_or_404(Stylesheet, id=id)
	form = StylesheetForm(request.POST or None, instance=instance)
	if form.is_valid():
		form.save()

	return render(request, 'edit-stylesheet.html', {
		'form': form,
		})


@login_required
def manage_stylesheets(request):
	stylesheets = Stylesheet.objects.all()

	return render(request, 'manage-stylesheets.html', {
		'stylesheets': stylesheets,
		})


@login_required
def delete_stylesheet(request, id):
	instance = get_object_or_404(Stylesheet, id=id)
	instance.delete()

	return redirect(manage_stylesheets)