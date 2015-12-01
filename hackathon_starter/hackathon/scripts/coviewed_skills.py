import urllib2
from bs4 import BeautifulSoup
import hashlib
import time
import os
import urllib
import hashlib

from utils import create_hash_string, get_url_data_with_retries, get_url_data, fetch_save_urls

def create_linkedin_skills_url(skill):
    encodelist = []
    for x in skill.strip().split(" "):
        encodelist.append(urllib.quote_plus(x))
    slug = '-'.join(encodelist)
    url = 'https://www.linkedin.com/topic/' + slug
    return url


#path = os.path.join(os.path.abspath(os.path.dirname('__file__')), "hackathon_starter", "hackathon", "static", "data", 'download_slug_list.txt')
#input_file = os.path.join(os.path.abspath(os.path.dirname('__file__')), "hackathon", "static", "data", 'download_slug_list.txt')
#output_dir = os.path.join(os.path.abspath(os.path.dirname('__file__')), "hackathon", "static", "data", 'download')


#fetch_save_urls(input_file, output_dir, create_linkedin_skills_url)
