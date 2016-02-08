from django.conf.urls import patterns, url, include

from hackathon import views

# urls.py
from django.views.generic import TemplateView
 
#from allauth
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
admin.autodiscover()


urlpatterns = patterns('',
    #url(r'^$', views.index, name='index'),
    url(r'^home/$', views.index, name='index'),
    url(r'^interview-skills-tool/$', views.skillsTool, name='skillsTool'),
    url(r'^interview-skills-tool/skills_api$', views.skills_api, name='skills_api'),
    url(r'^interview-skills-tool/amazon_reading_api$', views.amazon_reading_api, name='amazon_reading_api'),
    url(r'^interview-skills-tool/monster_skill_api$', views.monster_skill_api, name='monster_skill_api'),
    url(r'^interview-skills-tool/cover_letter_api$', views.cover_letter_api, name='cover_letter_api'),
    
    
    url(r'^how-it-works/$', views.howItWorks, name='howItWorks'),
    url(r'^pricing/$', views.pricing, name='pricing'),
    url(r'^about-us/$', views.aboutUs, name='aboutUs'),
    url(r'^get-started/$', views.getStarted, name='getStarted'),
    url(r'^customers/$', views.customers, name='customers'),
    
    url(r'^meet-our-counselors/$', views.meetOurCounselors, name='meetOurCounselors'),
    url(r'^online-tools/$', views.onlineTools, name='onlineTools'),
    url(r'^online-tools/interview-questions/$', views.interviewQuestions, name='interviewQuestions'),
    url(r'^online-tools/full-list-interview-questions/$', views.fullListIntQuestions, name='fullListIntQuestions'),
    
    url(r'^online-tools/mock-interview/$', views.mockInterview, name='mockInterview'),
    url(r'^online-tools/predict-my-future/$', views.predictFuture, name='predictFuture'),
    url(r'^online-tools/predict-my-future/predict_future_api$', views.predict_future_api, name='predict_future_api'),
    
    
    url(r'^start/join/', views.startJoin, name='startJoin'),
    
    
    #url(r'^blog/$', views.blog, name='blog'),
    url(r'^blog/', include('zinnia.urls', namespace='zinnia')),
    url(r'^comments/', include('django_comments.urls')),
    
    url(r'^privacy-policy/$', views.privacy_policy, name='privacy_policy'),
    
    
    
    #registration views
    #url(r'^register/$', views.register, name='register'),
    #url(r'^login/$', views.user_login, name='login'),
    #url(r'^logout/$', views.user_logout, name='logout'),
    
    #
    #url(r'^api/$', views.api_examples, name='api'),
    #url(r'^steam/$', views.steam, name='steam'),
    #url(r'^steamDiscountedGames/$', views.steamDiscountedGames, name='steamDiscountedGames'),
    #url(r'^githubResume/$', views.githubResume, name='githubResume'),
    #url(r'^githubUser/$', views.githubUser, name='githubUser'),
    #url(r'^githubTopRepositories/$', views.githubTopRepositories, name='githubTopRepositories'),
    #url(r'^tumblr/$', views.tumblr, name='tumblr'),
    #url(r'^linkedin/$', views.linkedin, name='linkedin'),
    #url(r'^snippets/$', views.snippet_list, name='snippets'),
    #url(r'^twilio/$', views.twilio, name='twilio'),
    #url(r'^instagram/$', views.instagram, name='instagram'),
    #url(r'^instagram_login/$', views.instagram_login, name='instagram_login'),
    #url(r'^instagramUser/$', views.instagramUser, name='instagramUser'),
    #url(r'^instagramMediaByLocation/$', views.instagramMediaByLocation, name='instagramMediaByLocation'),#
    #url(r'^instagramUserMedia/$', views.instagramUserMedia, name='instagramUserMedia'),
    #url(r'^twitter/$', views.twitter, name='twitter'),
    #url(r'^twitterTweets/$', views.twitterTweets, name='twitterTweets'),
    #url(r'^tumblr_login/$', views.tumblr_login, name='tumblr_login'),
    #url(r'^twitter_login/$', views.twitter_login, name='twitter_login'),
    #url(r'^github_login/$', views.github_login, name='github_login'),
    #url(r'^linkedin_login/$', views.linkedin_login, name='linkedin_login'),
    
    
    #url(r'^accounts/profile', views.facebook_profile, name='facebook_profile'),
    #url(r'^facebook_login/$', views.facebook_login, name='facebook_login'),
    #url(r'^facebook/$', views.facebook, name='facebook'),
    #url(r'^accounts/', include('allauth.urls')),

    #
    #
    #url(r'^google_login/$', views.google_login, name='google_login'),
    #url(r'^google/$', views.googlePlus, name='googlePlus'),
    #url(r'^dropbox_login/$', views.dropbox_login, name='dropbox_login'),
    #url(r'^dropbox/$', views.dropbox, name='dropbox'),
    #url(r'^dropboxSearchFile/$', views.dropboxSearchFile, name='dropboxSearchFile'),
    #url(r'^foursquare_login/$', views.foursquare_login, name='foursquare_login'),
    #url(r'^foursquare/$', views.foursquare, name='foursquare'),
    #url(r'^quandlSnp500/$', views.quandlSnp500, name='quandlsnp500'),
    #url(r'^quandlNasdaq/$', views.quandlNasdaq, name='quandlnasdaq'),
    #url(r'^quandlNasdaqdiff/$', views.quandlNasdaqdiff, name='quandlnasdaqdiff'),
    #url(r'^quandlDowJones/$', views.quandlDowJones, name='quandldowjones'),
    #url(r'^quandlstocks/$', views.quandlstocks, name='quandlstocks'),
    #url(r'^quandlapple/$', views.quandlapple, name='quandlapple'),
    #url(r'^quandlapplediff/$', views.quandlapplediff, name='quandlapplediff'),
    #url(r'^quandlDowJonesdiff/$', views.quandlDowJonesdiff, name='quandldowjonesdiff'),
    #url(r'^quandlSnp500diff/$', views.quandlSnp500diff, name='quandlsnp500diff'),
    #url(r'^nytimespop/$', views.nytimespop, name='nytimespop'),
    #url(r'^nytimestop/$', views.nytimestop, name='nytimestop'),
    #url(r'^nytimesarticles/$', views.nytimesarticles, name='nytimesarticles'),
    #url(r'^meetup/$', views.meetup, name='meetup'),
    #url(r'^meetupToken/$', views.meetupToken, name='meetupToken'),
    #url(r'^meetupUser/$', views.meetupUser, name='meetupUser'),
    #url(r'^yelp/$', views.yelp, name='yelp'),
)

#urlpatterns += patterns('',
#    url(r'^robots\.txt$', direct_to_template,
#    {'template': 'robots.txt', 'mimetype': 'text/plain'}),
#)


urlpatterns += patterns('',
    url(r'^robots\.txt$', TemplateView.as_view(template_name='content/robots.txt', content_type='text/plain'), name="robots"),
)


urlpatterns += patterns('',
    url(r'^$', views.landing_index, name='landing_index'),
    url(r'^about$', TemplateView.as_view(template_name='visitor/landing-about.html'), name='landing_about'),
    url(r'^terms/$', TemplateView.as_view(template_name='visitor/terms.html'), name='website_terms'),
    url(r'^contact$', TemplateView.as_view(template_name='visitor/contact.html'), name='website_contact'),
    
    (r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/$', 'authdemo.views.account_profile', name='account_profile'),
 
    url(r'^member/$', views.member_index, name='user_home'),
    url(r'^member/action$', views.member_action, name='user_action'),

    url(r'^admin/', include(admin.site.urls)),
    
    
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

