from django.db import models
from django.contrib.sites.models import Site
from django.contrib.auth.models import User


class PageTemplate(models.Model):

	title = models.CharField(max_length=100)
	template_content = models.TextField()

	def __unicode__(self):
		return self.title


class UserTemplate(models.Model):

	title = models.CharField(max_length=100)
	template_content = models.TextField()
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.title


class Page(models.Model):

	title = models.CharField(max_length=100)
	slug = models.SlugField(unique=True)
	meta_description = models.TextField(max_length=155)
	main_image = models.URLField()
	head_content = models.TextField()
	main_content = models.TextField()
	css = models.TextField()
	footer_content = models.TextField()
	sites = models.ManyToManyField(Site)
	comments = models.BooleanField()
	page_template = models.ForeignKey(PageTemplate)
	user_template = models.ForeignKey(UserTemplate, blank=True, null=True)

	def __unicode__(self):
		return self.title

	def template(self):
		return 'pagetemplates/' + str(self.page_template).lower() + '.html'
	

class PageMedia(models.Model):

	title = models.CharField(max_length=100)
	media = models.FileField(upload_to='/flatterpages/')
	media_type = models.CharField(max_length=50)
	url = models.URLField()
	page = models.ForeignKey(Page)

	def __unicode__(self):
		return self.title