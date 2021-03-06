

## See if monster can help



##Python libraries
import urllib2
import urllib
import string

##external
from bs4 import BeautifulSoup

#Internal libraries
from utils import create_hash_string, get_url_data_with_retries, get_url_data, fetch_save_urls, get_coviewed_skill
from hackathon.models import CoviewedSkills
from coviewed_skills import create_linkedin_skills_url
#Global variables



    


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
    
    monster_output = []
    for skill in m_related_skills:
        monster_output.append({"skill_name" : skill, "coviewed_model" : get_coviewed_skill(skill), "website": create_linkedin_skills_url(skill)})
    
    print monster_output
    return monster_output



