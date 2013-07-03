from django.contrib import admin

from flatterpages.models import Page, PageMedia, PageTemplate, UserTemplate, Stylesheet


class PageMediaInline(admin.TabularInline):
	model = PageMedia


class PageManager(admin.ModelAdmin):
	inlines = [
		PageMediaInline,
	]


admin.site.register(Page, PageManager)
admin.site.register(PageTemplate)
admin.site.register(UserTemplate)
admin.site.register(Stylesheet)