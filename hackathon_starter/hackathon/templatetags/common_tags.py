import json
from django import template
from myjobs.templatetags.common_tags import *
register = template.Library()


@register.simple_tag
def replace_base_url(value):
    return_value = value.replace('https://ss3.4sqi.net/img/categories_v2/', 'https://foursquare.com/img/categories/')
    return_value += "64.png"
    replacement_images = {
        'https://foursquare.com/img/categories/shops/mall_64.png': 'https://cdn1.iconfinder.com/data/icons/sales-and-shopping/32/bag_mall_web_ecommerce-64.png',
'https://foursquare.com/img/categories/parks_outdoors/plaza_64.png': 'https://cdn4.iconfinder.com/data/icons/unigrid-flat-buildings/90/008_092_kids_park_slides-64.png',
'https://foursquare.com/img/categories/education/communitycollege_64.png': 'https://cdn2.iconfinder.com/data/icons/educatix-circular/128/education_school_college-06-64.png',
'https://foursquare.com/img/categories/shops/departmentstore_64.png': 'https://cdn4.iconfinder.com/data/icons/buildings-vol-2-1/256/82-64.png',
'https://foursquare.com/img/categories/building/government_monument_64.png': 'https://cdn2.iconfinder.com/data/icons/jetflat-buildings/90/008_007_government_administration_official_building-64.png',
'https://foursquare.com/img/categories/education/other_64.png': 'https://cdn1.iconfinder.com/data/icons/education-colored-icons-vol-3/128/113-64.png',
        'https://foursquare.com/img/categories/shops/market_64.png': 'https://cdn3.iconfinder.com/data/icons/yellow-commerce/100/.svg-14-64.png',
'https://foursquare.com/img/categories/food/mediterranean_64.png': 'https://cdn3.iconfinder.com/data/icons/fruits-and-veggies-1/512/olive_meditteranean_food_oil_plant-64.png',
'https://foursquare.com/img/categories/education/academicbuilding_64.png': 'https://cdn3.iconfinder.com/data/icons/building-set-1/512/School-64.png',
'https://foursquare.com/img/categories/shops/conveniencestore_64': 'https://cdn2.iconfinder.com/data/icons/buildings-6/88/05-64.png',
'https://foursquare.com/img/categories/shops/food_gourmet_64.png': 'https://cdn2.iconfinder.com/data/icons/food-ink/512/salami-128.png',
    }
    try:
        print "trying stuff"
        return replacement_images[return_value]
    except KeyError:
        return return_value
        

@register.filter
def divide(value, arg):
    return (int(value) / int(arg)) if int(arg)!=0 else 0



@register.assignment_tag(takes_context=True)
def gz(context):
    request = context.get('request', None)
    if request == None or settings.DEBUG:
        return ''
    ae = request.META.get('HTTP_ACCEPT_ENCODING', '')
    if 'gzip' in ae:
        return ''
        # We've stopped returning .gz because of a bug in IE11 which causes
        # the static files to not be loaded at all. No longer serving .gz
        # files will also give us the opportunity to see what impact the
        # static files actually have on load time.
        # return '.gz'
    else:
        return ''

#COPIED OVER

import json

from time import strptime, strftime
from django import template
from django.conf import settings

from myjobs import version

#from myjobs.models import User
from authdemo.models import DemoUser as User

from myjobs.helpers import get_completion, make_fake_gravatar

#from seo.models import Company
#from universal.helpers import get_company

from django.db.models.loading import get_model




@register.simple_tag
def cache_buster():
    cache_buster = "?v=%s" % version.cache_buster
    return cache_buster


@register.simple_tag
def completion_level(level):
    """
    Determines the color of progress bar that should display.

    inputs:
    :level: The completion percentage of a user's profile.

    outputs:
    A string containing the bootstrap bar type
    """

    return get_completion(level)

@register.assignment_tag
def can(user, company, *activity_names):
    """Template tag analog to `myjobs.User.can()` method."""

    return user.can(company, *activity_names)


@register.simple_tag
def get_description(module):
    """
    Gets the description for a module.

    inputs:
    :module: The module to get the description for.

    outputs:
    The description for the module, or an empty string if the module or the
    description doesn't exist.
    """

    try:
        model = get_model("myprofile", module)
        return model.module_description if model.module_description else ""
    except Exception:
        return ""


@register.assignment_tag
def is_a_group_member(company, user, group):
    """
    Determines whether or not the user is a member of a group

    Inputs:
    :user: User instance
    :group: String of group being checked for

    Outputs:
    Boolean value indicating whether or not the user is a member of the
    requested group
    """

    if settings.ROLES_ENABLED:
        # deleted users don't have a PK
        return user.pk and user.roles.exists()
    else:
        try:
            return User.objects.is_group_member(user, group)
        except ValueError:
            return False


@register.assignment_tag
def get_company_name(user):
    """
    Gets the name of companies associated with a user

    Inputs:
    :user: User instance

    Outputs:
    A `QuerySet` of companies for which the user is a `CompanyUser`.
    """

    # Only return companies for which the user is a company user
    if settings.ROLES_ENABLED:
        return Company.objects.filter(role__user=user).distinct()
    else:
        try:
            return user.company_set.all()
        except ValueError:
            return Company.objects.none()


@register.simple_tag(takes_context=True)
def active_tab(context, view_name):
    """
    Determines whether a tab should be highlighted as the active tab.

    Inputs:
    :view_name: The name of the view, as a string, for the tab being evaluated.

    Outputs:
    Either "active" if it's the active tab, or an empty string.
    """

    return "active" if context.get('view_name', '') == view_name else ""


@register.simple_tag
def get_gravatar(user, size=20):
    """
    Gets the img or div tag for the gravatar or initials block.
    """
    try:
        return user.get_gravatar_url(size)
    except:
        return ''


@register.simple_tag
def get_nonuser_gravatar(email, size=20):
    try:
        return make_fake_gravatar(email, size)
    except:
        return ''


@register.assignment_tag(takes_context=True)
def get_ms_name(context):
    """
    Gets the site name for the user's last-visited microsite, if one exists
    """
    request = context.get('request')
    cookie = request.COOKIES.get('lastmicrositename')
    if cookie and len(cookie) > 33:
        cookie = cookie[:30] + '...'
    return cookie


@register.simple_tag(takes_context=True)
def get_ms_url(context):
    """
    Gets the url for the user's last-visited microsite from a cookie,
    or www.my.jobs if that cookie does not exist.
    """
    request = context.get('request')
    cookie = request.COOKIES.get('lastmicrosite')
    if cookie:
        return cookie
    return 'http://www.my.jobs'


@register.simple_tag
def str_to_date(string):
    try:
        return strftime("%b. %d %Y", strptime(string, "%Y-%m-%dT%H:%M:%SZ"))
    except:
        return strftime("%b. %d %Y", strptime(string, "%Y-%m-%dT%H:%M:%S.%fZ"))



@register.simple_tag
def date_to_str(t):
    try:
        return t.strftime('%b %Y')
    except:
        print "Had trouble converting string"
        return t


@register.simple_tag
def to_string(value):
    return str(value)


@register.filter
def get_attr(obj, attr):
    return obj.get(attr)


@register.simple_tag
def paginated_index(index, page, per_page=None):
    """
    Given an index, page number, and number of items per page, returns a proper
    index.

    inputs:
    :index: The index you are converting from. Should be less than `per_page`.
    :page: The page for which you want to calculate the new index
    :per_page: Number of records per page

    outputs:
    New index which takes pagination into consideration.
    """

    per_page = int(per_page or 10)
    page = int(page or 1) - 1
    index = int(index or 1)
    return page * per_page + index


@register.assignment_tag(takes_context=True)
def gz(context):
    request = context.get('request', None)
    if request == None or settings.DEBUG:
        return ''
    ae = request.META.get('HTTP_ACCEPT_ENCODING', '')
    if 'gzip' in ae:
        return ''
        # We've stopped returning .gz because of a bug in IE11 which causes
        # the static files to not be loaded at all. No longer serving .gz
        # files will also give us the opportunity to see what impact the
        # static files actually have on load time.
        # return '.gz'
    else:
        return ''


@register.assignment_tag
def json_companies(companies):
    info = [{"name": company.name, "id": company.id} for company in companies]
    return json.dumps(info)


@register.filter
def get_suggestions(user):
    """
    Get all profile suggestions for the given user, sorted by profile importance

    Inputs:
    :user: User for whom suggestions will be retrieved

    Outputs:
    :suggestions: List of profile suggestions
    """
    suggestions = [suggestion for suggestion in
                   user.profileunits_set.model.suggestions(user,
                                                           by_priority=False)
                   if suggestion['priority'] == 5]
    return suggestions


@register.assignment_tag(takes_context=True)
def get_company_from_cookie(context):
    request = context.get('request')
    if request:
        return get_company(request)
    return None

