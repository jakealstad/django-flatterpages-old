from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', TemplateView.as_view(template_name='flatterpages/base.html')),

    # Examples:
    # url(r'^$', 'flatterpages.views.home', name='home'),
    # url(r'^flatterpages/', include('flatterpages.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^$', 'flatterpages.views.manage_pages'),
	url(r'^create-page/$', 'flatterpages.views.create_page'),
    url(r'^edit-page/(?P<url>.*)/(?P<pk>.*)/$', 'flatterpages.views.edit_page'),
    url(r'^create-sub-page/(?P<url>.*)/$', 'flatterpages.views.create_sub_page'),
    url(r'^manage-pages/$', 'flatterpages.views.manage_pages'),
	url(r'^delete-page/(?P<url>.*)/(?P<pk>.*)/$', 'flatterpages.views.delete_page'),
    url(r'^create-page-template/$', 'flatterpages.views.create_page_template'),
    url(r'^create-user-template/$', 'flatterpages.views.create_user_template'),
    url(r'^edit-page-template/(?P<id>.*)/$', 'flatterpages.views.edit_page_template'),
    url(r'^edit-user-template/(?P<id>.*)/$', 'flatterpages.views.edit_user_template'),
    url(r'^manage-page-templates/$', 'flatterpages.views.manage_page_templates'),
    url(r'^manage-user-templates/$', 'flatterpages.views.manage_user_templates'),
    url(r'^delete-page-template/(?P<id>.*)/$', 'flatterpages.views.delete_page_template'),
    url(r'^delete-user-template/(?P<id>.*)/$', 'flatterpages.views.delete_user_template'),
    url(r'^create-stylesheet/$', 'flatterpages.views.create_stylesheet'),
    url(r'^edit-stylesheet/(?P<id>.*)/$', 'flatterpages.views.edit_stylesheet'),
    url(r'^manage-stylesheets/$', 'flatterpages.views.manage_stylesheets'),
    url(r'^delete-stylesheet/(?P<id>.*)/$', 'flatterpages.views.delete_stylesheet'),
    url(r'^get-parent-page/(?P<title>.*)/$', 'flatterpages.views.get_parent_page'),
    url(r'^search/.*$', 'flatterpages.views.search'),
    url(r'^filter/.*$', 'flatterpages.views.filter'),
	# url(r'^(?P<url>.*)/$', 'flatterpages.views.render_page'),
)