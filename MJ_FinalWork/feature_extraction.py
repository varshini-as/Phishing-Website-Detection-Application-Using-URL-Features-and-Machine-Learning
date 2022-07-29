import datetime
import ipaddress
import time
from typing import List
from urllib.parse import urlparse
import pandas as pd
import whois
import re
from bs4 import BeautifulSoup
import requests

HINTS = ['wp', 'login', 'includes', 'admin', 'content', 'site', 'images', 'js', 'alibaba', 'css', 'myaccount', 'dropbox', 'themes', 'plugins', 'signin', 'view']
#################################################################################################################################
#               URL hostname length 
#################################################################################################################################

def url_length(url):
    return len(url) 

#################################################################################################################################
#               Having IP address in hostname
#################################################################################################################################

def having_ip_address(url):
    match = re.search(
        '(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.'
        '([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|'  # IPv4
        '((0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\/)|'  # IPv4 in hexadecimal
        '(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}|'
        '[0-9a-fA-F]{7}', url)  # Ipv6
    if match:
        return 1
    else:
        return 0

#################################################################################################################################
#              Count number of dots in hostname
#################################################################################################################################

def count_dots(hostname):
    return hostname.count('.')

#################################################################################################################################
#               Count dash (-) symbol at base url
#################################################################################################################################

def count_hyphens(base_url):
    return base_url.count('-')

#################################################################################################################################
#               Count at (@) symbol at base url
#################################################################################################################################

def count_at(base_url):
     return base_url.count('@')
 

#################################################################################################################################
#              Count number of qm in hostname
#################################################################################################################################

def count_qm(hostname):
    return hostname.count('?')

#################################################################################################################################
#               Count and (&) symbol at base url (Das'19)
#################################################################################################################################

def count_and(base_url):
     return base_url.count('&')

#################################################################################################################################
#               Count equal (=) symbol at base url
#################################################################################################################################

def count_equal(base_url):
    return base_url.count('=')

#################################################################################################################################
#               Count percentage (%) symbol at base url (Chiew2019)
#################################################################################################################################

def count_percentage(base_url):
    return base_url.count('%')

#################################################################################################################################
#               Count slash (/) symbol at full url
#################################################################################################################################

def count_slash(full_url):
    return full_url.count('/')

#################################################################################################################################
#              Count number of colon (:) symbol
#################################################################################################################################

def count_colon(url):
    return url.count(':')


#################################################################################################################################
#               Having semicolumn (;) symbol at base url
#################################################################################################################################

def count_semicolumn(url):
     return url.count(';')
 
    
#################################################################################################################################
#               count www in url words (Sahingoz2019)
#################################################################################################################################

def check_www(words_raw):
        count = 0
        for word in words_raw:
            if not word.find('www') == -1:
                count += 1
        return count
   
    
#################################################################################################################################
#               count com in url words (Sahingoz2019)
#################################################################################################################################

def check_com(url):
    return url.count('.com')
        

#################################################################################################################################
#               Count redirection (//) symbol at full url
#################################################################################################################################

def count_double_slash(full_url):
    list=[x.start(0) for x in re.finditer('//', full_url)]
    if list[len(list)-1]>6:
        return 1
    else:
        return 0
    return full_url.count('//')


#################################################################################################################################
#               Uses https protocol
#################################################################################################################################

def https_token(scheme):
    if scheme == 'https':
        return 0
    return 1

#################################################################################################################################
#               prefix suffix
#################################################################################################################################

def prefix_suffix(url):
    if re.findall(r"https?://[^\-]+-[^\-]+/", url):
        return 1
    else:
        return 0
    
#################################################################################################################################
#               number of phish-hints in url path 
#################################################################################################################################

def phish_hints(url_path):
    count = 0
    for hint in HINTS:
        count += url_path.lower().count(hint)
    return count
#################################################################################################################################
#               URL shortening
#################################################################################################################################

def shortening_service(full_url):
    match = re.search('bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|'
                      'yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|'
                      'short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|'
                      'doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|'
                      'db\.tt|qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|'
                      'q\.gs|is\.gd|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|'
                      'x\.co|prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|'
                      'tr\.im|link\.zip\.net',
                      full_url)
    if match:
        return 1
    else:
        return 0
##################################################################################################################################
#            whois_registered_domain
##################################################################################################################################
def whois_registered_domain(url):
  try:
    domain = urlparse(url).netloc
    domain_name = whois.whois(domain)
    domainResponse = domain_name.domain_name
    try:
      if type(domainResponse) == list:
        for host in domainResponse:
          if re.search(host.lower(), domain):
            return 0
        return 1
      else:
        if re.search(domainResponse.lower(),domain):
          return 0
        else:
          return 1
    except:
      return 1
  except:
    return 1

#################################################################################################################################
#               Google index
#################################################################################################################################

from urllib.parse import urlencode

proxies = {
    'https' : 'https://158.69.53.132:9300',
    'http' : 'http://158.69.53.132:9300'
    }

def google_index(url):
    time.sleep(.6)
    user_agent =  'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
    headers = {'User-Agent' : user_agent}
    query = {'q': 'info:' + url}
    google = "https://www.google.com/search?" + urlencode(query)
    # data = requests.get(google, headers=headers)
    data = requests.get(google, headers=headers, proxies=proxies)
    data.encoding = 'ISO-8859-1'
    soup = BeautifulSoup(str(data.content), "html.parser")
    # print(soup)
    # try:
    #     if 'Our systems have detected unusual traffic from your computer network.' in str(soup):
    #         return -1
    #     check = soup.find(id="rso").find("div").find("div").find("a")
    #     print(check)
    #     if check and check['href']:
    #         return 0
    #     else:
    #         return 1
    try:
        # check = soup.find(id="rso").find("div").find("div").find("div").find("div").find("div").find("a")["href"]
        check = soup.find(id="rso").find("div").find("div").find("h3").find("a")
        href = check['href']
        print("URL is Index ")
        return 0
    except AttributeError:
        print("URL Not Index")
        return 1
        
    # except AttributeError:
    #     return 1

#print(google_index('http://www.google.com'))

#################################################################################################################################
#               Domain age of a url
#################################################################################################################################

import json

"""def domainAge(url):
  domain = urlparse(url).netloc
  domain_name = whois.whois(domain)
  #print(type(domain_name.creation_date))
  creation_date = domain_name.creation_date
  expiration_date = domain_name.expiration_date
  if ((expiration_date is None) or (creation_date is None)):
      return -1
  else:  
    ageofdomain = abs((expiration_date - creation_date).days)
  return ageofdomain"""

def domainAge(url):
    try:
        domain = urlparse(url).netloc
        #print(domain)
        domain_name = whois.whois(domain)
        #print(type(domain_name.creation_date))
        creation_date = domain_name.creation_date
        expiration_date = domain_name.expiration_date
        if ((expiration_date is None) or (creation_date is None)):
            return -1
        else:
            if type(creation_date) == list:
                creation_date = creation_date[0]
            if type(expiration_date) == list:
                expiration_date = expiration_date[0]
            ageofdomain = abs((expiration_date - creation_date).days)
            return ageofdomain
    except:
        return -1

#################################################################################################################################
#               Unable to get web traffic (Page Rank)
#################################################################################################################################
import urllib

# def web_traffic(short_url):
#         try:
#             rank = BeautifulSoup(urllib.request.urlopen("http://data.alexa.com/data?cli=10&dat=s&url=" + short_url).read(), "xml").find("REACH")['RANK']
#         except:
#             return 0
#         return int(rank)

#def web_traffic(url):
 # try:
  #Filling the whitespaces in the URL if any
#    url = urllib.parse.quote(url)
#    rank = BeautifulSoup(urllib.request.urlopen("http://data.alexa.com/data?cli=10&dat=s&url=" + url).read(), "xml").find(
#        "REACH")['RANK']
#    rank = int(rank)
#    return rank
#  except TypeError:
#        return 0
#   if rank >100000:
#     return 1
#   else:
#     return 0

def web_traffic(short_url):
    try:
        rank = BeautifulSoup(urllib.request.urlopen("http://data.alexa.com/data?cli=10&dat=s&url=" + short_url).read(), "xml").find("REACH")['RANK']
    except:
        return 0
    return int(rank)




#Function to extract features
def featureExtraction(url):
  parsed = urlparse(url)
  scheme = parsed.scheme
  domain = urlparse(url).netloc
  words_raw = re.split("\-|\.|\/|\?|\=|\@|\&|\%|\:|\_", domain.lower())
  features = []
  #features.append(url)
  features.append(url_length(url))
  features.append(having_ip_address(url))
  features.append(count_dots(url))
  features.append(count_hyphens(url))
  features.append(count_at(url))
  features.append(count_qm(url))
  features.append(count_and(url))
  features.append(count_equal(url))
  features.append(count_percentage(url))
  features.append(count_slash(url))
  features.append(count_colon(url))
  features.append(count_semicolumn(url))
  features.append(check_www(words_raw))
  features.append(check_com(url))
  features.append(count_double_slash(url))
  features.append(https_token(scheme))
  features.append(prefix_suffix(url))
  features.append(phish_hints(url))
  features.append(shortening_service(url))
  features.append(whois_registered_domain(url))
#  features.append(google_index(url))
  features.append(domainAge(url))
  features.append(web_traffic(url))
  return features

#def generateExcel():
#  headers = ['URL', 'Have_IP', 'Have_At', 'URL_Length', 'URL_Depth', 'Redirection', 'https_In_Domain', 'TinyURL', 'Prefix/Suffix', 
#              'Have_Https_Token', 'Hyphens_Count', 'WHOIS_Registered', 'Domain_Age']
#
#  df = pd.DataFrame(columns= headers)
#  url_df = pd.read_csv('phishing_dataset_1.csv', usecols=['url'])
#  url_list = url_df['url'].tolist()
#
#  for url in url_list:
#    classification = featureExtraction(url)
#    df.loc[len(df)] = classification     # append to last empty column
#    print(len(df))
  
#  df.to_csv('extracted.csv', index= False)

#generateExcel()

# url= "http://opfkduzdrw.duckdns.org"
#print(web_traffic(url))
#print(whois_registered_domain(url))
# f=featureExtraction(url)
# print(f)


