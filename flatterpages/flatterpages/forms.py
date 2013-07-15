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
		super(PageForm, self).__init__(*args, **kwargs)

	def save(self, do_redirect=False, commit=True):
		instance = super(PageForm, self).save(commit=commit)
		write_to_file(instance, 'css')

		return instance


class PageTemplateForm(forms.ModelForm):

	class Meta:
		model = PageTemplate

	def __init__(self, *args, **kwargs):
		super(PageTemplateForm, self).__init__(*args, **kwargs)

	def save(self, commit=True):
		instance = super(PageTemplateForm, self).save(commit=commit)
		write_to_file(instance, 'html')

		return instance


class UserTemplateForm(forms.ModelForm):

	class Meta:
		model = UserTemplate

	def __init__(self, *args, **kwargs):
		super(UserTemplateForm, self).__init__(*args, **kwargs)

	def save(self, commit=True):
		instance = super(UserTemplateForm, self).save(commit=commit)
		return instance


class StylesheetForm(forms.ModelForm):

	class Meta:
		model = Stylesheet

	def __init__(self, *args, **kwargs):
		super(StylesheetForm, self).__init__(*args, **kwargs)

	def save(self, commit=True):
		instance = super(StylesheetForm, self).save(commit=commit)
		return instance