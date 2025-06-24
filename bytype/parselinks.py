"""Demonstrate regex replace by line"""
import re

#file = 'best_practices.html'
#file = 'conference_presentations.html'
#file = 'documents.html'
#file = 'replication_resources.html'
#file = 'trainings.html'
#file = 'webinar.html'
file = 'website.html'
with open(file,'r',encoding='utf-8') as myinfile:
  lines = myinfile.read().splitlines()


url_set = set()

# find and report
for thisline in lines:
  branch = re.search(r"<span\s+class=\"field-content\">\s*<a\s+href=\"(.*?)\"",thisline)
  if branch:
    thisurl = 'https://targethiv.org' + branch.group(1)
    url_set.add(thisurl)

## find and report
#for thisline in lines:
#  newline = re.sub(r"\W","",thisline)
#  print(newline)

url_list = list(url_set)

url_list.sort()

for thisurl in url_list[0:100]:
#for thisurl in url_list[100:200]:
#for thisurl in url_list[200:300]:
#for thisurl in url_list[300:400]:
#for thisurl in url_list[400:500]:
#for thisurl in url_list[500:600]:
#for thisurl in url_list[600:700]:
#for thisurl in url_list[700:800]:
#for thisurl in url_list[800:900]:
#for thisurl in url_list[900:1000]:
#for thisurl in url_list[1000:1100]:
#for thisurl in url_list[1100:1200]:
  print(thisurl)
