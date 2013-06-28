from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html')),

    # Examples:
    # url(r'^$', 'flatterpages.views.home', name='home'),
    # url(r'^flatterpages/', include('flatterpages.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^flatterpages/$', 'flatterpages.views.manage_pages'),
	url(r'^flatterpages/create-page/$', 'flatterpages.views.create_page'),
    url(r'^flatterpages/edit-page/(?P<slug>.*)$', 'flatterpages.views.edit_page'),
    url(r'^flatterpages/manage-pages/$', 'flatterpages.views.manage_pages'),
	url(r'^flatterpages/delete-page/(?P<slug>.*)$', 'flatterpages.views.delete_page'),
    url(r'^flatterpages/create-page-template/$', 'flatterpages.views.create_page_template'),
    url(r'^flatterpages/create-user-template/$', 'flatterpages.views.create_user_template'),
    url(r'^flatterpages/edit-page-template/(?P<id>.*)$', 'flatterpages.views.edit_page_template'),
    url(r'^flatterpages/edit-user-template/(?P<id>.*)$', 'flatterpages.views.edit_user_template'),
    url(r'^flatterpages/manage-page-templates$', 'flatterpages.views.manage_page_templates'),
    url(r'^flatterpages/manage-user-templates$', 'flatterpages.views.manage_user_templates'),
    url(r'^flatterpages/delete-page-template/(?P<id>.*)$', 'flatterpages.views.delete_page_template'),
    url(r'^flatterpages/delete-user-template/(?P<id>.*)$', 'flatterpages.views.delete_user_template'),
	url(r'^(?P<slug>.*)$', 'flatterpages.views.render_page'),
)