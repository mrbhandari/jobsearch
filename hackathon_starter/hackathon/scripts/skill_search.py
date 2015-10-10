#imports
from urllib import quote
from urllib2 import Request, urlopen, URLError
import string
import json
from itertools import tee, izip
from nltk import PorterStemmer
from nltk.stem import RegexpStemmer
from  more_itertools import unique_everseen
from collections import Counter
import re
import os
from coviewed_skills import create_linkedin_skills_url

#global vars
STEMMING_ON = True
STEMMING_LIMIT = 6
request_string = 'https://www.linkedin.com/ta/skill?query='
#skills_path = 'skill_data.json'
#job_path = 'employment.txt'


def ngrams(input_string, n):
  output = []
  for i in range(len(input_string)-n+1):
    output.append(input_string[i:i+n])
  return output

def join_ngram(input_string, n):
    return [' '.join(x) for x in ngrams(input_string, n)] # ['a b', 'b c', 'c d']

def stemmed_word(word):
   
    if STEMMING_ON == True and len(word)>STEMMING_LIMIT:
      #st = RegexpStemmer('ing$|s$|e$|able$', min=STEMMING_LIMIT)
      try:
        return PorterStemmer().stem_word(word.lower())
        #return st.stem(word)
      except:
        pass
    else:
        return word
      
def autosuggest_api(i):
  ## takes a query and pings linkedin api for autosuggest results - returns display names that match that query
  master_skills_list = []
  request = Request( request_string+ quote(i))
  response = urlopen(request)
  matched_skills = response.read()
  json_data = json.loads(matched_skills)
  for j in json_data.get('resultList'):
    master_skills_list.append(j.get('displayName'))
  return master_skills_list


def fetch_skill_api():
    
    list_of_files = ['pre_6.txt']
    
    #list_of_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    
    for i in list_of_files:
      master_skills_list = []
      i_path_join = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "static", "data", i)
      with open(i_path_join, 'r') as fp:
        contents = fp.readlines()
        #print contents
        for line in contents:
          print line
          master_skills_list.extend(autosuggest_api(line))
      
      print master_skills_list
      
      
      c = list(unique_everseen(master_skills_list))
      ioutput_path_join = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "static", "data", i + 'out')
      
      with open(ioutput_path_join, 'w') as fp:
        for item in c:
          fp.write("%s\n" % item)
    
    

def generate_candidates(job_text, term_lenght):
    ngrams = {}
    #with open(job_path, 'r') as f:
    #for line in job_text:
    words = re.split('\s+|/|\n+', job_text.strip()) #TODO: test if this works
    
    if term_lenght == 1:
      return words
    else:
      return join_ngram(words, term_lenght)
    
    return ngrams
    
def find_matching_skills(job_text, skills_path):
    job_text = job_text.lower()
    matched_skills_linkedin, all_skills, blacklist_skills = [], [], []
    
    skills_path_join = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "static", "data", skills_path)
    blacklist_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "static", "data", "blacklist.txt")
    
    with open(blacklist_path, 'r') as fp:
        for line in fp:
            blacklist_skills.append(line.lower().strip())
    
    with open(skills_path_join, 'r') as fp:
        for line in fp:
            all_skills.append(line.lower().strip())
            
    for x in blacklist_skills:
      all_skills.remove(x)
    
    all_skills_stemmed = [stemmed_word(i) for i in all_skills]
    
    
 
  
    max_num_terms = 3
    
    while max_num_terms > 0:
      print ["starting", max_num_terms]
      all_candidates = generate_candidates(job_text, max_num_terms)
      
      for f in all_candidates:
        try:
            if all_skills_stemmed.index(stemmed_word(f)):
                relevant_skill = all_skills[all_skills_stemmed.index(stemmed_word(f))]
                matched_skills_linkedin.append(relevant_skill)
                job_text = job_text.replace(f, '')
        
        
        except ValueError, e:
            pass
      
      max_num_terms = max_num_terms -1
      #print job_text.encode('utf-8')
      skills_counter= Counter(matched_skills_linkedin)
      print skills_counter
      if max_num_terms == 0:
        break
    

    
    
    return skills_counter
  
  
def rank_skills(data):
  #takes a skills counter and sorts it with two terms or greater at top, rest below sub sorted by frequency
  output_list_end = list()
  output_list_beg = list()
  
  for key in data:
      terms = len(key.split())
      if terms < 2:
        output_list_end.append({'name': key, 'terms': terms, 'frequency': int(data[key]), 'website': create_linkedin_skills_url(key)})
  output_list_end = sorted(output_list_end, key=lambda output_list_end: output_list_end['frequency'], reverse=True)
  
  for key in data:
      terms = len(key.split())
      if terms >= 2:
          output_list_beg.append({'name': key, 'terms': terms, 'frequency': int(data[key]), 'website': create_linkedin_skills_url(key)})
  output_list_beg = sorted(output_list_beg, key=lambda output_list_beg: output_list_beg['frequency'], reverse=True)
  
  return {'important': output_list_beg, 'not_important': output_list_end}
  

#execute
#fetch_skill_api()
#find_matching_skills(job_path, skills_path)
