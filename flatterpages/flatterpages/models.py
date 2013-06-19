from django.db import models
from django.contrib.sites.models import Site


class PageTemplate(models.Model):

	title = models.CharField(max_length=100)
	template_content = models.TextField()


class Page(models.Model):

	title = models.CharField(max_length=100)
	slug = models.SlugField()
	meta_description = models.TextField(max_length=155)
	main_image = models.URLField()
	head_content = models.TextField()
	main_content = models.TextField()
	css = models.TextField()
	footer_content = models.TextField()
	sites = models.ManyToManyField(Site)
	comments = models.BooleanField()
	template = models.ForeignKey(PageTemplate)
	

class PageMedia(models.Model):

	title = models.CharField(max_length=100)
	media = models.FileField(upload_to='/flatterpages/')
	media_type = models.CharField(max_length=50)
	url = models.URLField()
	page = models.ForeignKey(Page)