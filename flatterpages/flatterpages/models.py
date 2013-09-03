import json

from django.db import models
from django.contrib.sites.models import Site
from django.contrib.auth.models import User


class PageTemplate(models.Model):

	title = models.CharField(max_length=100)
	main_content = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	last_updated_by = models.ForeignKey(User)
	path = models.CharField(max_length=200, blank=True, null=True)

	def __unicode__(self):
		return self.title


class Stylesheet(models.Model):
	
	title = models.CharField(max_length=100)
	css = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	last_updated_by = models.ForeignKey(User)
	path = models.CharField(max_length=200)

	def __unicode__(self):
		return self.title


class UserTemplate(models.Model):

	title = models.CharField(max_length=100)
	css = models.TextField()
	main_content = models.TextField()
	user = models.ForeignKey(User)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	global_css = models.ForeignKey(Stylesheet, blank=True, null=True)

	def __unicode__(self):
		return self.title


class Page(models.Model):

	parent_page = models.ForeignKey('self', blank=True, null=True)
	title = models.CharField(max_length=100)
	url = models.CharField(max_length=100)
	meta_description = models.TextField(max_length=155)
	main_image = models.URLField()
	head_content = models.TextField(blank=True, null=True)
	main_content = models.TextField()
	css = models.TextField(blank=True, null=True)
	footer_content = models.TextField(blank=True, null=True)
	sites = models.ManyToManyField(Site)
	comments = models.BooleanField()
	page_template = models.ForeignKey(PageTemplate)
	user_template = models.ForeignKey(UserTemplate, blank=True, null=True, on_delete=models.SET_NULL)
	stylesheet = models.ForeignKey(Stylesheet, blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	last_updated_by = models.ForeignKey(User)

	def __unicode__(self):
		return self.title

	def template(self):
		return self.page_template.path
	

class PageMedia(models.Model):

	title = models.CharField(max_length=100)
	media = models.FileField(upload_to='/flatterpages/')
	media_type = models.CharField(max_length=50)
	url = models.URLField()
	page = models.ForeignKey(Page)

	def __unicode__(self):
		return self.title