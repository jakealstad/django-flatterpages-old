import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.template import Context, Template

from flatterpages.forms import PageForm, PageTemplateForm, UserTemplateForm, StylesheetForm
from flatterpages.models import Page, PageMedia, PageTemplate, UserTemplate, Stylesheet


@login_required
def create_page(request):
	if request.method == 'POST':
		form = PageForm(request.POST)
		if form.is_valid():
			if 'save' in form.data:
				form.save()
				return redirect(manage_pages)
			elif 'save_and_continue' in form.data:
				form.save()
				# redirect to edit view to prevent multiple copies of Page
				return redirect(edit_page, url=form.data['url'])
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
		if 'save' in form.data:
			form.save()
			return redirect(manage_pages)
		elif 'save_and_continue' in form.data:
			form.save()
	
	user_templates = UserTemplate.objects.filter(user=request.user)

	return render(request, 'edit-page.html', {
		'form': form,
		'user_templates': user_templates,
		'page': instance,
		})


@login_required
def create_sub_page(request, url):
	instance = get_object_or_404(Page, url=url)

	return render(request, 'edit-page.html', {
		'instance': instance,
		})


def render_page(request, url):
	page = get_object_or_404(Page, url=url)

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
			return redirect(manage_page_templates)

	else:
		form = PageTemplateForm()

	return render(request, 'edit-template.html', {
		'form': form,
		})


@login_required
def create_user_template(request):
	if request.method == 'POST':
		css_dict = {
			'title': request.POST['title'],
			'css': request.POST['css'],
			'last_updated_by': request.POST['user'],
		}
		css_form = StylesheetForm(css_dict)
		template_form = UserTemplateForm(request.POST)
		if template_form.is_valid():
			template_form.save()
			css_form.save()
			return redirect(manage_user_templates)

	else:
		template_form = UserTemplateForm()

	return render(request, 'edit-template.html', {
		'form': template_form,
		})


@login_required
def edit_page_template(request, id):
	instance = get_object_or_404(PageTemplate, id=id)
	form = PageTemplateForm(request.POST or None, instance=instance)
	if form.is_valid():
		form.save()
		return redirect(manage_page_templates)

	return render(request, 'edit-template.html', {
		'form': form,
		'template': instance,
		})


@login_required
def edit_user_template(request, id):
	instance = get_object_or_404(UserTemplate, id=id)
	form = UserTemplateForm(request.POST or None, instance=instance)
	if form.is_valid():
		form.save()
		return redirect(manage_user_templates)

	return render(request, 'edit-template.html', {
		'form': form,
		'template': instance,
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


@login_required
def get_parent_page(request, title):
	page = get_object_or_404(Page, title=title)
	
	parent_page = {
		'title': page.title,
		'url': page.url,
		'meta_description': page.meta_description,
		'main_image': page.main_image,
		'head_content': page.head_content,
		'main_content': page.main_content,
		'css': page.css,
		'footer_content': page.footer_content,
		'sites': str(page.sites),
		'page_template': str(page.page_template),
		'user_template': page.user_template,
		'stylesheet': page.stylesheet,
		'last_updated_by': str(page.last_updated_by),
	}

	page = json.dumps(parent_page)

	return HttpResponse(page, mimetype='application/json')
