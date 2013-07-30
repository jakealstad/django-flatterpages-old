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
		initial = kwargs.get('initial', {})
		initial['css'] = kwargs['instance'].stylesheet.css
		kwargs['initial'] = initial
		super(PageForm, self).__init__(*args, **kwargs)

		# print self.instance.stylesheet

		# if self.instance.stylesheet:
		# 	print 'setting from global stylesheet'
		# 	self.fields["css"].initial = self.instance.stylesheet.css

	def save(self, commit=False):
		instance = super(PageForm, self).save(commit=commit)
		write_to_file(instance, 'css')

		if instance.stylesheet == None:
			print 'creating new stylesheet'
			new_stylesheet = Stylesheet(title=instance.title, css=instance.css, last_updated_by=instance.last_updated_by)
			new_stylesheet.page = instance
			new_stylesheet.save()
			instance.stylesheet = new_stylesheet
			instance.save()
		else:
			print 'updating existing stylesheet'
			update_stylesheet = Stylesheet.objects.get(pk=instance.stylesheet.pk)
			update_stylesheet.css = instance.css
			update_stylesheet.save()
			instance.save()

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