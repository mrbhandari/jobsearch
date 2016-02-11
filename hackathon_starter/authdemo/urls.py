from django.conf.urls import patterns, url, include

from hackathon import views
from myprofile import views as myprofileviews

# urls.py
from django.views.generic import TemplateView
 
#from allauth
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
admin.autodiscover()



urlpatterns = patterns('',
    url(r'^$', views.landing_index, name='landing_index'),
    url(r'^about$', TemplateView.as_view(template_name='visitor/landing-about.html'), name='landing_about'),
    url(r'^terms/$', TemplateView.as_view(template_name='visitor/terms.html'), name='website_terms'),
    url(r'^contact$', TemplateView.as_view(template_name='visitor/contact.html'), name='website_contact'),
    
    (r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/$', 'authdemo.views.account_profile', name='account_profile'),
 
    url(r'^member/$', myprofileviews.edit_profile, name='user_home'), #views.member_index
    url(r'^member/action$', views.member_action, name='user_action'),

    url(r'^admin/', include(admin.site.urls)),
    
    
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)