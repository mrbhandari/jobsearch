from django.db import models
from django.contrib.auth.models import User

#for all auth http://www.sarahhagstrom.com/2013/09/the-missing-django-allauth-tutorial/#Display_the_user8217s_Facebook_or_Gravatar_icon
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount
import hashlib


# Create your models here.



 
class UserProfile(models.Model):
    # Relations
    user = models.OneToOneField(User, related_name='profile')
    
    
    # Attributes - Mandatory
    zipcode = models.PositiveIntegerField(default=0,
                                          )
    age = models.PositiveIntegerField(default=0,
                                          )
    currently_employed = models.BooleanField(default=False,
                                          )
    paid_job_before = models.BooleanField(default=False,
                                          )
    #Education level
    NO_HS = 'NO'
    HIGHSCHOOL = 'HS'
    COLLEGE = 'BA'
    EDUCATION_LEVEL_CHOICES = (
        (NO_HS, 'Less than highschool'),
        (HIGHSCHOOL, 'Highschool completed'),
        (COLLEGE, "Bachelor's degree"),
    )
    education_level = models.CharField(max_length=2,
                                      choices=EDUCATION_LEVEL_CHOICES,
                                      default=NO_HS)


    #currently_studying
    #hours_preferred
    #hours_preferred = ("Part time", "Casual", "Fulltime", "Holidays/seasonal")

 
    class Meta:
        db_table = 'user_profile'
    
    # Custom Properties
    def account_verified(self):
        if self.user.is_authenticated:
            result = EmailAddress.objects.filter(email=self.user.email)
            if len(result):
                return result[0].verified
        return False

    def profile_image_url(self):
        fb_uid = SocialAccount.objects.filter(user_id=self.user.id, provider='facebook')
        print "XXXXXXXXXXXXs"
        print fb_uid
     
        if len(fb_uid):
            return "http://graph.facebook.com/{}/picture?width=40&height=40".format(fb_uid[0].uid)
     
        return "http://www.gravatar.com/avatar/{}?s=40".format(hashlib.md5(self.user.email).hexdigest())
    
    # Methods
    
    # Meta and String
    class Meta:
        pass
    
    def __unicode__(self):
        return "{}'s profile".format(self.user.username)
 



User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])






class CoviewedSkills(models.Model):
    source_skill = models.CharField(max_length=2000)
    target_skill = models.CharField(max_length=2000)
    target_skill_count = models.IntegerField(max_length=10)
    target_skill_rank = models.IntegerField(max_length=5, default= 0)
    filename = models.CharField(max_length=2000)

    def __unicode__(self):
        return unicode(self.source_skill)
    
    
    
    
#
#class Profile(models.Model):
#    user = models.ForeignKey(User)
#    oauth_token = models.CharField(max_length=200)
#    oauth_secret = models.CharField(max_length=200)
#
#    def __unicode__(self):
#        return unicode(self.user)
#
#class GithubProfile(models.Model):
#    user = models.ForeignKey(User)
#    github_user = models.CharField(max_length=200)
#    access_token = models.CharField(max_length=200)
#    scopes = models.CharField(max_length=200)
#
#    def __unicode__(self):
#        return unicode(self.user)
#
#class TumblrProfile(models.Model):
#    user = models.ForeignKey(User)
#    tumblr_user = models.CharField(max_length=200)
#    access_token = models.CharField(max_length=200)
#    access_token_secret = models.CharField(max_length=200)
#
#    def __unicode__(self):
#        return unicode(self.user)
#
#class InstagramProfile(models.Model):
#    user = models.ForeignKey(User)
#    instagram_user = models.CharField(max_length=200)
#    access_token = models.CharField(max_length=200)
#
#    def __unicode__(self):
#        return unicode(self.user)
#
#class TwitterProfile(models.Model):
#    user = models.ForeignKey(User)
#    twitter_user = models.CharField(max_length=200)
#    oauth_token = models.CharField(max_length=200)
#    oauth_token_secret = models.CharField(max_length=200)
#
#    def __unicode__(self):
#        return unicode(self.user)
#
#class LinkedinProfile(models.Model):
#    user = models.ForeignKey(User)
#    linkedin_user = models.CharField(max_length=200)
#    access_token = models.CharField(max_length=200)
#
#    def __unicode__(self):
#        return unicode(self.user)
#
class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)

#class MeetupToken(models.Model):
#    # user = models.ForeignKey(User)
#    access_token = models.CharField(max_length=200)
#
#    def __unicode__(self):
#        return unicode(self.access_token)
#
#class FacebookProfile(models.Model):
#    user = models.ForeignKey(User)
#    fb_user_id = models.CharField(max_length=100)
#    time_created = models.DateTimeField(auto_now_add=True)
#    profile_url = models.CharField(max_length=50)
#    access_token = models.CharField(max_length=100)
#
#class GoogleProfile(models.Model):
#    user = models.ForeignKey(User)
#    google_user_id = models.CharField(max_length=100)
#    time_created = models.DateTimeField(auto_now_add=True)
#    access_token = models.CharField(max_length=100)
#    profile_url = models.CharField(max_length=100)
#
#class DropboxProfile(models.Model):
#    user = models.ForeignKey(User)
#    dropbox_user_id = models.CharField(max_length=100)
#    time_created = models.DateTimeField(auto_now_add=True)
#    access_token = models.CharField(max_length=100)
#
#
#class FoursquareProfile(models.Model):
#    user = models.ForeignKey(User)
#    foursquare_id = models.CharField(max_length=100)
#    time_created = models.DateTimeField(auto_now_add=True)
#    access_token = models.CharField(max_length=100)
