from django.contrib import admin

from flatterpages.models import Page, PageMedia, PageTemplate


class PageMediaInline(admin.TabularInline):
	model = PageMedia


class PageManager(admin.ModelAdmin):
	inlines = [
		PageMediaInline,
	]
	prepopulated_fields = {"slug": ("title",)}


admin.site.register(Page, PageManager)
admin.site.register(PageTemplate)