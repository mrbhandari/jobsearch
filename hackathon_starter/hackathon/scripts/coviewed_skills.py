import urllib2
from bs4 import BeautifulSoup
import hashlib
import time
import os
import urllib
import hashlib


def get_url_data(url):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Googlebot'), ('Cookie', 'bcookie="v=2&a4dbb96f-4c7b-4d2a-88b2-32cc9abdf6d4"')]
    f = opener.open(url)
    data = f.read()
    return data

def get_url_data_with_retries(url, n):
    url_data = None
    for i in range(0,n):
        try:
            url_data = get_url_data(url)
        except urllib2.HTTPError as e:
            print "sleeping for 30 seconds because of httperror",e
            time.sleep(30)
        except Exception as e:
            return None
        if url_data is not None:
            return url_data
    return None

def create_hash_string(url):
    m = hashlib.md5()
    m.update(url)
    return str(m.hexdigest())


def create_linkedin_skills_url(skill):
    encodelist = []
    for x in skill.strip().split(" "):
        encodelist.append(urllib.quote_plus(x))
    slug = '-'.join(encodelist)
    url = 'https://www.linkedin.com/topic/' + slug
    return url

def execute():
    path = os.path.join(os.path.abspath(os.path.dirname('__file__')), "hackathon_starter", "hackathon", "static", "data", 'download_slug_list.txt')
    print path
    with open(path,'r') as f:
        for i in f.readlines():
            url = create_linkedin_skills_url(i)
            print url
            fn = create_hash_string(url) + '.html'
            path = os.path.join(os.path.abspath(os.path.dirname('__file__')), "hackathon_starter", "hackathon", "static", "data", 'download', fn)
            with open(path, 'w') as f:
                try:
                    f.write(get_url_data_with_retries(url, 3))
                except TypeError as e:
                    print e 
                    print "failed\t " + i
                except Exception as e:
                    print e
                    print "failed\t " + i