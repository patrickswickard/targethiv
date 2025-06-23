"""Simple requests demo"""
import requests
import re
from datetime import datetime

request_url1 = 'https://targethiv.org/resources?at-y8cIiWa0=iBxDfkAB&at-iBxDfkAB=gX9qoaiz&at-gX9qoaiz=ReC6UofA&at-ReC6UofA=tzg&antibot_key=zgAtof6UeCzRaiqoX9BgkADfBx0iWaIi8cey814gFos&f[0]=topic_areas_for_resources_search_block%3A1653&at-sFo4g81e=y8cIiWa0&page=1'
request_url2 = 'https://targethiv.org/'
request_url3 = 'https://targethiv.org/library/ehe-scp-innovative-approaches-clinical-care'
text_result = requests.get(request_url3).text
print(text_result)
