from django import forms
from django.contrib.sites.models import Site
from django.contrib.auth.models import User, Group

from flatterpages.models import Page, PageMedia, PageTemplate, UserTemplate


class PageForm(forms.ModelForm):

	class Meta:
		model = Page

	def __init__(self, *args, **kwargs):
		super(PageForm, self).__init__(*args, **kwargs)

	def save(self, commit=True):
		instance = super(PageForm, self).save(commit=commit)
		return instance


class PageTemplateForm(forms.ModelForm):

	class Meta:
		model = PageTemplate

	def __init__(self, *args, **kwargs):
		super(PageTemplateForm, self).__init__(*args, **kwargs)

	def save(self, commit=True):
		instance = super(PageTemplateForm, self).save(commit=commit)
		f = open('templates/pagetemplates/' + str(instance.title).lower() + '.html', 'w')
		f.write(instance.main_content)
		f.close()

		return instance


class UserTemplateForm(forms.ModelForm):

	class Meta:
		model = UserTemplate

	def __init__(self, *args, **kwargs):
		super(UserTemplateForm, self).__init__(*args, **kwargs)

	def save(self, commit=True):
		instance = super(UserTemplateForm, self).save(commit=commit)
		return instance