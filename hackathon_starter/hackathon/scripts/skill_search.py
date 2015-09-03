#imports
from urllib import quote
from urllib2 import Request, urlopen, URLError
import string
import json
from itertools import tee, izip
from nltk import PorterStemmer
from  more_itertools import unique_everseen
from collections import Counter
import re
import os

#global vars
STEMMING_ON = True
STEMMING_LIMIT =6
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
        try:
            result = PorterStemmer().stem_word(word.lower())
            return PorterStemmer().stem_word(word.lower())
        except:
            pass
    else:
        return word

def fetch_skill_api():
    master_skills_list = []
    
    list_of_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    
    for a in list_of_letters:
        for b in list_of_letters:
            i  = a + b
            request = Request( request_string+ quote(i))
            response = urlopen(request)
            matched_skills = response.read()
            json_data = json.loads(matched_skills)
            for j in json_data.get('resultList'):
                master_skills_list.append(j.get('displayName'))
    
    
    c = list(unique_everseen(master_skills_list))
    with open(skills_path, 'w') as fp:
        json.dump(c, fp)

def generate_candidates(job_text):
    ngrams = []
    #with open(job_path, 'r') as f:
    #for line in job_text:
    words = re.split('\s+|/|\n+', job_text.strip()) #TODO: test if this works
    ngrams += words + join_ngram(words, 2) + join_ngram(words, 3)
    return ngrams
    
def find_matching_skills(job_text, skills_path):
    matched_skills_linkedin, all_skills= [], []
    
    all_candidates = generate_candidates(job_text)
    print all_candidates
    print "The current working directory is", os.getcwd()
    skills_path_join = os.path.join(os.getcwd(), "hackathon", "static", "data", skills_path)
    print skills_path_join
    with open(skills_path_join, 'r') as fp:
        for line in fp:
            all_skills.append(line.lower().strip())
    
    all_skills_stemmed = [stemmed_word(i) for i in all_skills]
    
    for f in all_candidates:
        try:
            if all_skills_stemmed.index(stemmed_word(f.lower())):
                relevant_skill = all_skills[all_skills_stemmed.index(stemmed_word(f.lower()))]
                matched_skills_linkedin.append(relevant_skill)
        
        except ValueError, e:
            pass
   
    c= Counter(matched_skills_linkedin)
    
    print c
    return c

#execute
#find_matching_skills(job_path, skills_path)
