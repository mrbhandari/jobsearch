
import urllib2
from bs4 import BeautifulSoup
import hashlib
import time
import os
import urllib
import hashlib


def create_hash_string(url):
    m = hashlib.md5()
    m.update(url)
    return str(m.hexdigest())

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


def fetch_save_urls(input_file, output_dir, createURL):
    with open(input_file,'r') as f:
        for i in f.readlines():
            url = createURL(i)
            print url
            fn = create_hash_string(url) + '.html'
            path = os.path.join(output_dir, fn)
            with open(path, 'w') as f:
                try:
                    f.write(get_url_data_with_retries(url, 3))
                except TypeError as e:
                    print e 
                    print "failed\t " + i
                except Exception as e:
                    print e
                    print "failed\t " + i
