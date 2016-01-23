#test django context
from django.template import Template, Context, loader
import math
from operator import itemgetter
from collections import Counter


#generate google search result urls
def get_request_urls(query_string, num_results):
    list_of_request_urls = []
    max_page = min(int(math.ceil(num_results/10)), 50)
    for i in range(0, max_page):

        encode_query_string = query_string.replace('"', '%22').replace(" ", '+')
        smriti_pace = 'https://www.googleapis.com/customsearch/v1?q=' + encode_query_string + '&key=AIzaSyBYVngMReah5qDa3j-ZZqpwkvxJ-7gYecs&cx=016438211762245286972%3Ar0phxcqd2gg&start='
        avani_google_base_url = 'https://www.googleapis.com/customsearch/v1?q=masters+molecular+biology+MBA+"San+Francisco"&key=AIzaSyBYVngMReah5qDa3j-ZZqpwkvxJ-7gYecs&cx=016438211762245286972%3Ar0phxcqd2gg&start='.replace('"', '%22').replace(" ", '+')
        test_google_base_url = 'https://www.googleapis.com/customsearch/v1?q="inventory+coordinator"&key=AIzaSyBYVngMReah5qDa3j-ZZqpwkvxJ-7gYecs&cx=016438211762245286972%3Ar0phxcqd2gg&start='.replace('"', '%22')
        rahul_future_google_base_url = 'https://www.googleapis.com/customsearch/v1?q=CTO+"San+Francisco"&key=AIzaSyBYVngMReah5qDa3j-ZZqpwkvxJ-7gYecs&cx=016438211762245286972%3Ar0phxcqd2gg&start='.replace('"', '%22')
        general_google_base_url = 'https://www.googleapis.com/customsearch/v1?q="founder"+"CTO"+"San+Francisco"&key=AIzaSyBYVngMReah5qDa3j-ZZqpwkvxJ-7gYecs&cx=016438211762245286972%3Ar0phxcqd2gg&start='.replace('"', '%22')
        pradeep_google_base_url = 'https://www.googleapis.com/customsearch/v1?q="founder"+"data+scientist"+"San+Francisco"&key=AIzaSyBYVngMReah5qDa3j-ZZqpwkvxJ-7gYecs&cx=016438211762245286972%3Ar0phxcqd2gg&start='.replace('"', '%22')
        devanshi_google_base_url = 'https://www.googleapis.com/customsearch/v1?q="head+of+marketing"+OR++"VP+of+Marketing"+"San+Francisco"+mckinsey+OR+facebook&key=AIzaSyBYVngMReah5qDa3j-ZZqpwkvxJ-7gYecs&cx=016438211762245286972%3Ar0phxcqd2gg&start='.replace('"', '%22')
        rahul_google_base_url = 'https://www.googleapis.com/customsearch/v1?q=Mckinsey+Product+Manager&key=AIzaSyBYVngMReah5qDa3j-ZZqpwkvxJ-7gYecs&cx=016438211762245286972%3Ar0phxcqd2gg&start='
        smriti_google_base_url = 'https://www.googleapis.com/customsearch/v1?q=university+of+tulsa+MIS+-professor&key=AIzaSyBYVngMReah5qDa3j-ZZqpwkvxJ-7gYecs&cx=016438211762245286972%3Ar0phxcqd2gg&start='
        list_of_request_urls.append(smriti_pace+ str(i*10+1))
    print list_of_request_urls
    return list_of_request_urls




## import stuff
import urllib2
import urllib
import json
from bs4 import BeautifulSoup






def generate_google_urls(query_string, num_results):
    list_of_urls = []
    for request_urls in get_request_urls(query_string, num_results):
        datak = json.load(urllib2.urlopen(request_urls))
        for i in datak['items']:
            list_of_urls.append(i['link'])

    print list_of_urls
    return list_of_urls
    
    
    
    
    
import hashlib
import time
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



def counter_to_list(counter_obj, maximum_len):
    counter_obj_list_counter = list(Counter(counter_obj).items())
    counter_obj_list_counter_sorted = sorted(counter_obj_list_counter, key=itemgetter(1), reverse=True)
    return counter_obj_list_counter_sorted[:25]



def generate_summary(query_string, num_results):
    #list_of_urls = [u'https://www.linkedin.com/pub/jason-parker-j-d/26/43/101']
    #full_text_corpus = ''
    skills_agg, companies_agg, titles_agg, schools_agg, degrees_agg = [], [], [], [], []
    master_dump = []
    linkedin_URLs = generate_google_urls(query_string, num_results)
    
    for url in linkedin_URLs:
        print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        print url
        output = get_url_data_with_retries(url, 3)
        soup = BeautifulSoup(output)
    
        education_line = []
        experience_line = []
        skills_line = []
        
        
        try:
            ss_education = soup.find("section", {"id": "education"}).find_all("li")
            for i in ss_education:
                
                school, degree = '', ''
                for x in i.find_all("time"):
                    education_line.append(x.get_text())
                for x in i.find_all("h4"):
                    school = x.get_text()
                    education_line.append(school)
                    schools_agg.append(school)
                for x in i.find_all("h5"):
                    degree = x.get_text()
                    education_line.append(degree)
                    degrees_agg.append(degree)
                print education_line
        except:
            pass

        try:
            ss_experience = soup.find("section", {"id": "experience"}).find_all("li")    
            for i in ss_experience:
                
                title, company = '', ''
                for x in i.find_all("time"):
                    experience_line.append(x.get_text())
                for x in i.find_all("h4"):
                    title = x.get_text()
                    experience_line.append(title)
                    titles_agg.append(title)

                for x in i.find_all("h5"):
                    company = x.get_text()
                    experience_line.append(company)
                    companies_agg.append(company)

                #experience_line.append(i.find("p", {"class": "description"}).get_text())
                print experience_line    
        except:
            pass

        try:
            ss_skills = soup.find("section", {"id": "skills"}).find_all("li")
            
            for i in ss_skills:
                skills_line.append(i.get_text())
            skills_agg += skills_line
            print skills_line
        except:
            pass
        
        master_dump.append({'url': url, 'education': education_line, 'experience': experience_line, 'skills': skills_line })
    

    print "XXXXX TOP SKILS XXXXX"
    print Counter(skills_agg)

    print "XXXXX TOP COMPANIES XXXXX"
    print Counter(companies_agg)

    print "XXXXX TOP TITLES XXXXX"
    print Counter(titles_agg)

    print "XXXXX TOP SCHOOLS XXXXX"
    print Counter(schools_agg)

    print "XXXXX TOP DEGREES XXXXX"
    print Counter(degrees_agg)
    
    print "XXXXX MASTER DUMP XXXXX"
    
    print master_dump


    
    
    return {'skills_agg': counter_to_list(skills_agg, 25),
            'companies_agg': counter_to_list(companies_agg, 25),
            'titles_agg': counter_to_list(titles_agg, 25),
            'schools_agg': counter_to_list(schools_agg, 25),
            'degrees_agg': counter_to_list(degrees_agg, 25),
            'urls': linkedin_URLs,
            'master_dump': master_dump,
    }
    #get global skills
    #skills_counter = find_matching_skills(full_text_corpus, skills_file)
    #sorted_data = rank_skills(skills_counter)



