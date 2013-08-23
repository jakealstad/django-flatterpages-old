import json

from django.contrib.auth.decorators import login_required
from django.contrib.sites.models import Site
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.template import Context, Template

from flatterpages.forms import PageForm, PageTemplateForm, UserTemplateForm, StylesheetForm
from flatterpages.models import Page, PageMedia, PageTemplate, UserTemplate, Stylesheet
from flatterpages.utils import normalize_query, get_query


@login_required
def create_page(request):
    if request.method == 'POST':
        form = PageForm(request.POST, user=request.user)
        if form.is_valid():
            if 'save' in form.data:
                form.save()
                form.save_m2m()
                return redirect(manage_pages)
            elif 'save_and_continue' in form.data:
                form.save()
                form.save_m2m()
                # redirect to edit view to prevent multiple copies of Page
                return redirect(edit_page, url=form.data['url'])
    else:
        form = PageForm(user=request.user)

    user_templates = UserTemplate.objects.filter(user=request.user)

    return render(request, 'flatterpages/edit-page.html', {
        'form': form,
        'user_templates': user_templates,
        })


@login_required
def edit_page(request, url, pk):
    instance = get_object_or_404(Page, url=url, pk=pk)
    form = PageForm(request.POST or None, instance=instance, user=request.user)
    if form.is_valid():
        if 'save' in form.data:
            form.save()
            form.save_m2m()
            return redirect(manage_pages)
        elif 'save_and_continue' in form.data:
            form.save()
            form.save_m2m()
    
    user_templates = UserTemplate.objects.filter(user=request.user)

    return render(request, 'flatterpages/edit-page.html', {
        'form': form,
        'user_templates': user_templates,
        'page': instance,
        })


@login_required
def create_sub_page(request, url):
    if request.method == 'POST':
        form = PageForm(request.POST, user=request.user)
        if form.is_valid():
            if 'save' in form.data:
                form.save()
                form.save_m2m()
                return redirect(manage_pages)
            elif 'save_and_continue' in form.data:
                form.save()
                form.save_m2m()
                return redirect(edit_page, url=form.data['url'])
    else:
        instance = get_object_or_404(Page, url=url)
        form = PageForm(initial={
            'title': instance.title,
            'url': instance.url,
            'meta_description': instance.meta_description,
            'main_image': instance.main_image,
            'head_content': instance.head_content,
            'main_content': instance.main_content,
            'css': instance.css,
            'footer_content': instance.footer_content,
            # 'sites': instance.sites,
            'comments': instance.comments,
            'parent_page': instance,
            'page_template': instance.page_template,
            'user_template': instance.user_template,
            'stylesheet': instance.stylesheet,
            'last_updated_by': request.user,
            })

    return render(request, 'flatterpages/edit-page.html', {
        'form': form,
        })


def render_page(request, url):
    site = Site.objects.get_current()
    page = get_object_or_404(Page, url=url, sites__exact=site)

    return render(request, 'flatterpages/base.html', {
        'page': page,
        })


@login_required
def manage_pages(request):
    sites = Site.objects.all()
    pages = Page.objects.all()

    # site_list = [site for site in sites]
    # site_list.insert(0, '')

    return render(request, 'flatterpages/manage-pages.html', {
        'pages': pages,
        'sites': sites,
        })


@login_required
def delete_page(request, url):
    page = get_object_or_404(Page, url=url)
    page.delete()

    return redirect(manage_pages)


@login_required
def create_page_template(request):
    if request.method == 'POST':
        form = PageTemplateForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect(manage_page_templates)

    else:
        form = PageTemplateForm(user=request.user)

    return render(request, 'flatterpages/edit-template.html', {
        'form': form,
        })


@login_required
def create_user_template(request):
    if request.method == 'POST':
        css_dict = {
            'title': request.POST['title'],
            'css': request.POST['css'],
            'last_updated_by': request.POST['user'],
            'path': '.',
        }
        css_form = StylesheetForm(css_dict)
        template_form = UserTemplateForm(request.POST, user=request.user)
        if template_form.is_valid():
            template_form.save()
            css_form.save()
            return redirect(manage_user_templates)

    else:
        template_form = UserTemplateForm(user=request.user)

    return render(request, 'flatterpages/edit-template.html', {
        'form': template_form,
        })


@login_required
def edit_page_template(request, id):
    instance = get_object_or_404(PageTemplate, id=id)
    form = PageTemplateForm(request.POST or None, instance=instance, user=request.user)
    if form.is_valid():
        form.save()
        return redirect(manage_page_templates)

    return render(request, 'flatterpages/edit-template.html', {
        'form': form,
        'template': instance,
        })


@login_required
def edit_user_template(request, id):
    instance = get_object_or_404(UserTemplate, id=id)
    form = UserTemplateForm(request.POST or None, instance=instance, user=request.user)
    if form.is_valid():
        form.save()
        return redirect(manage_user_templates)

    return render(request, 'flatterpages/edit-template.html', {
        'form': form,
        'template': instance,
        })


@login_required
def manage_page_templates(request):
    templates = PageTemplate.objects.all()

    return render(request, 'flatterpages/manage-page-templates.html', {
        'templates': templates,
        })


@login_required
def manage_user_templates(request):
    templates = UserTemplate.objects.all()

    return render(request, 'flatterpages/manage-user-templates.html', {
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
        form = StylesheetForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
    else:
        form = StylesheetForm(user=request.user)

    return render(request, 'flatterpages/edit-stylesheet.html', {
        'form': form,
        })


@login_required
def edit_stylesheet(request, id):
    instance = get_object_or_404(Stylesheet, id=id)
    form = StylesheetForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()

    return render(request, 'flatterpages/edit-stylesheet.html', {
        'form': form,
        })


@login_required
def manage_stylesheets(request):
    stylesheets = Stylesheet.objects.all()

    return render(request, 'flatterpages/manage-stylesheets.html', {
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
        'sites': str(page.sites.all()),
        'page_template': str(page.page_template),
        'user_template': str(page.user_template),
        'stylesheet': str(page.stylesheet),
        'last_updated_by': str(page.last_updated_by),
    }

    page = json.dumps(parent_page)

    return HttpResponse(page, mimetype='application/json')


def search(request):
    query_string = ''
    found_pages = None
    site_filter = None
    page_query = None
    sites = Site.objects.all()

    if request.GET['site']:
        if not request.GET['site'].isdigit():
            site_filter = None
        else:
            site_filter = request.GET['site']

    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']

        page_query = get_query(query_string, ['title', 'url'])

    if site_filter or page_query:

        if page_query and site_filter:
            found_pages = Page.objects.filter(page_query, sites=site_filter).order_by('-updated')
        elif page_query and not site_filter:
            found_pages = Page.objects.filter(page_query).order_by('-updated')
        elif not page_query and site_filter:
            found_pages = Page.objects.filter(sites=site_filter).order_by('-updated')
        else:
            found_pages = []

        return_pages = []

        for page in found_pages:
            if page.parent_page:
                parent = page.parent_page
                if parent not in return_pages:
                    return_pages.append(parent)
            elif not page.parent_page and page not in return_pages:
                return_pages.append(page)

        return render(request, 'flatterpages/manage-pages.html', {
            'pages': return_pages,
            'sites': sites,
            'selected_site': site_filter,
            'query': query_string,
            })

    else:
        # return nothing if query is blank
        return render(request, 'flatterpages/manage-pages.html', {
            'pages': [],
            'sites': sites,
            })


def filter(request):
    if ('site' in request.GET) and request.GET['site'].strip():
        pk = request.GET['site']
        sites = Site.objects.all()
        site = get_object_or_404(Site, pk=pk)
        pages = Page.objects.filter(sites=site)

    return render(request, 'flatterpages/manage-pages.html', {
        'sites': sites,
        'pages': pages,
        })