from django import forms
from django.contrib.sites.models import Site
from django.contrib.auth.models import User, Group

from flatterpages.models import Page, PageMedia, PageTemplate


class PageForm(forms.ModelForm):

	class Meta:
		model = Page
		fields = [
			'title',
			'slug',
			'meta_description',
			'main_image',
			'head_content',
			'main_content',
			'css',
			'footer_content',
			'sites',
			'comments',
			'template',
		]

	def __init__(self, *args, **kwargs):
		super(PageForm, self).__init__(*args, **kwargs)

	def save(self, commit=True):
		instance = super(PageForm, self).save(commit=commit)
		return instance