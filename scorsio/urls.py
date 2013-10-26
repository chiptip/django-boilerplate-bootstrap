from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^assets/(?P<path>.*)$', 'django.views.static.serve', dict(document_root=settings.ASSET_ROOT)),
    url(r'^$', TemplateView.as_view(template_name='index.html'))
    # url(r'^scorsio/', include('scorsio.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
