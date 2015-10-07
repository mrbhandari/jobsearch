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
      st = RegexpStemmer('ing$|s$|e$|able$', min=STEMMING_LIMIT)
      try:
        result = PorterStemmer().stem_word(word.lower())
        return st.stem(word)
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
        print contents
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
    matched_skills_linkedin, all_skills= [], []
    
    
    
    
    
    skills_path_join = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "static", "data", skills_path)
    
    with open(skills_path_join, 'r') as fp:
        for line in fp:
            all_skills.append(line.lower().strip())
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
      c= Counter(matched_skills_linkedin)
      
      if max_num_terms == 0:
        break
    

    
    
    return c

#execute
#fetch_skill_api()
#find_matching_skills(job_path, skills_path)
