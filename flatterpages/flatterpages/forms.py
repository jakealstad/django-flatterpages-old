from os import path, mkdir

from django import forms
from django.contrib.sites.models import Site
from django.contrib.auth.models import User, Group

from flatterpages.models import Page, PageMedia, PageTemplate, UserTemplate, Stylesheet
from flatterpages.utils import write_to_file


class PageForm(forms.ModelForm):

	class Meta:
		model = Page

	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user', None)
		try:
			initial = kwargs.get('initial', {})
			initial['css'] = kwargs['instance'].stylesheet.css
			kwargs['initial'] = initial
		except KeyError:
			pass

		super(PageForm, self).__init__(*args, **kwargs)

		self.fields['last_updated_by'].initial = user

	def save(self, commit=False):
		instance = super(PageForm, self).save(commit=commit)

		# remove leading and trailing slashes
		url = str(instance.url).strip('/')
		instance.url = url

		# if no stylesheet for page, create one
		if instance.stylesheet == None:
			new_stylesheet = Stylesheet(title=instance.title, css=instance.css, last_updated_by=instance.last_updated_by)
			new_stylesheet.page = instance
			filepath = write_to_file(instance.title, instance, 'css')
			new_stylesheet.path = filepath
			new_stylesheet.save()
			instance.stylesheet = new_stylesheet
			instance.save()
		# update existing stylesheet
		else:
			update_stylesheet = Stylesheet.objects.get(pk=instance.stylesheet.pk)
			update_stylesheet.css = instance.css
			if instance.parent_page:
				filepath = write_to_file(instance.parent_page.title, instance, 'css')
			else:
				filepath = write_to_file(instance.title, instance, 'css')
			update_stylesheet.path = filepath
			update_stylesheet.save()
			# save all pages in the group
			instance.save()
			pages = instance.stylesheet.page_set.all()
			for page in pages:
				page.save()

		return instance


class PageTemplateForm(forms.ModelForm):

	class Meta:
		model = PageTemplate

	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user', None)
		super(PageTemplateForm, self).__init__(*args, **kwargs)
		self.fields['last_updated_by'].initial = user

	def save(self, commit=True):
		instance = super(PageTemplateForm, self).save(commit=commit)
		write_to_file(instance, 'html')

		return instance


class UserTemplateForm(forms.ModelForm):

	class Meta:
		model = UserTemplate

	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user', None)
		super(UserTemplateForm, self).__init__(*args, **kwargs)
		self.fields['user'].initial = user		

	def save(self, commit=True):
		instance = super(UserTemplateForm, self).save(commit=commit)
		return instance


class StylesheetForm(forms.ModelForm):

	class Meta:
		model = Stylesheet

	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user', None)
		super(StylesheetForm, self).__init__(*args, **kwargs)
		self.fields['last_updated_by'].initial = user

	def save(self, commit=True):
		instance = super(StylesheetForm, self).save(commit=commit)
		return instance