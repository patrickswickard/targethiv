"""Demonstrate regex replace by line"""
import re

#file = 'website.html'
file = 'conference_presentations.html'
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

for thisurl in url_set:
  print(thisurl)
