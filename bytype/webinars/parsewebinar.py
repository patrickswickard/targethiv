"""Demonstrate regex replace by line"""
import re
import glob
import os

#file = 'best_practices.html'
#file = 'conference_presentations.html'
#file = 'documents.html'
#file = 'replication_resources.html'
#file = 'trainings.html'
#file = 'webinar.html'
#file = 'website.html'
file1 = 'YGetIt_ Program _ TargetHIV.html'
file2 = 'What Works in HIV Care & Services Podcast _ TargetHIV.html'
file3 = 'The SPOT _ TargetHIV.html'

filelist = []

for file in os.listdir("/home/swickape/projects/github/targethiv/bytype/webinars/100"):
  if file.endswith(".html"):
    filelist.append(os.path.join("/home/swickape/projects/github/targethiv/bytype/webinars/100", file))
for file in os.listdir("/home/swickape/projects/github/targethiv/bytype/webinars/200"):
  if file.endswith(".html"):
    filelist.append(os.path.join("/home/swickape/projects/github/targethiv/bytype/webinars/200", file))
for file in os.listdir("/home/swickape/projects/github/targethiv/bytype/webinars/300"):
  if file.endswith(".html"):
    filelist.append(os.path.join("/home/swickape/projects/github/targethiv/bytype/webinars/300", file))
for file in os.listdir("/home/swickape/projects/github/targethiv/bytype/webinars/rest"):
  if file.endswith(".html"):
    filelist.append(os.path.join("/home/swickape/projects/github/targethiv/bytype/webinars/rest", file))

#print(filelist)

set_of_urls = set()

for thisfile in filelist:
  with open(thisfile,'r',encoding='utf-8') as myinfile:
    textblob = myinfile.read()
  textblob = ' '.join(textblob.splitlines())
  #print(textblob)
  #resourcere = re.search(r"<div\s+class=\"field__label\"\s*>Resources\s+&amp;\s+Tools\s*</div>\s*(.*?)</div>\s*</div>",textblob)
  resourcere = re.search(r"(.*)",textblob)
  if resourcere:
    resourceblob = resourcere.group(1)
    linklist = re.findall(r"(<a[^>]*href=.*?</a>)",resourceblob)

    for thislink in linklist:
      linkre = re.search(r"<a[^>]*href=\"(.*?)\"[^>]*>\s*(.*?)\s*</a>",thislink)
      if linkre:
        thisurl = linkre.group(1)
        thistitle = linkre.group(2)
        thisurlre = re.search(r"(https?://)",thisurl)
        if thisurlre:
          thisurl = thisurl
        else:
          thisurl = 'https://targethiv.org'
        set_of_urls.add(thisurl)
#      print(thistitle)
#      print(thisfile)
      #print(thislink)

url_list = list(set_of_urls)
url_list.sort()

for thisurl in url_list:
  print(thisurl)

