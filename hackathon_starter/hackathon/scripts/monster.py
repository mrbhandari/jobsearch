## See if monster can help

##Python libraries
import urllib2
import urllib
from bs4 import BeautifulSoup
import string


#Internal libraries
from utils import create_hash_string, get_url_data_with_retries, get_url_data, fetch_save_urls

#Global variables

#i = "Product Engagement Manager"


def generate_monster_url(job_title):
    url_base = "http://jobs.monster.com/search/?q="
    print job_title
    
    encodelist = []
    slug = ''
    
    remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
    word_list = [job_title.translate(remove_punctuation_map) for s in job_title.strip().split(" ")]
    print word_list
    print "XXXXXXXXXXXX"
    #.translate(None, string.punctuation).
    for x in job_title.translate(remove_punctuation_map).strip().split(" "):
        encodelist.append(urllib.quote_plus(x))
        slug = '-'.join(encodelist)
    url = url_base + slug
    return url

def parse_monster_url(job_title):
    url = generate_monster_url(job_title)
    output = get_url_data_with_retries(url, 3)
    soup = BeautifulSoup(output)
    ss = soup.find("li", {"id": "backlinkingwidgetSkill"}).find_all("li")
    m_related_skills = []
    for i in ss:
        m_related_skills.append(i.find("a").get_text())
        
    m_related_skills.remove("Show More")
    m_related_skills.remove("show less")
    print m_related_skills
    return m_related_skills
