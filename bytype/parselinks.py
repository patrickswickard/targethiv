"""Demonstrate regex replace by line"""
import re

file = 'website.html'
with open(file,'r',encoding='utf-8') as myinfile:
  lines = myinfile.read().splitlines()

# find and report
for thisline in lines:
  branch = re.search(r"<span\s+class=\"field-content\">\s*<a\s+href=\"(.*?)\"",thisline)
  if branch:
    print('https://targethiv.org' + branch.group(1))


## find and report
#for thisline in lines:
#  newline = re.sub(r"\W","",thisline)
#  print(newline)
