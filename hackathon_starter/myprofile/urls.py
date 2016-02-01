from django.conf.urls import patterns, url
from django.views.generic import RedirectView

urlpatterns = patterns('myprofile.views',
    url(r'^view/home$', RedirectView.as_view(url='/profile/view/')),
    url(r'^view$', 'edit_profile', name='view_profile'),
    url(r'^view/$', 'edit_profile', name='view_profile'),
    url(r'^view/delete$', 'delete_item', name='delete_item'),
    url(r'^view/edit$', 'handle_form', name='handle_form'),
    url(r'^view/details$', 'get_details', name='get_details'),
)


urlpatterns += patterns(
    'myjobs.views',
    url(r'^account/edit/$', 'edit_account', name='edit_account'),
    url(r'^account/delete$', 'delete_account', name='delete_account'),
    url(r'^account/disable$', 'disable_account', name='disable_account'),
)