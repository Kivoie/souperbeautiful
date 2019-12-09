import requests
from bs4 import BeautifulSoup
from newsapi import NewsApiClient
import json
newsapi = NewsApiClient(api_key='722fafcc38eb4c41aae3b84db65b4f77')

url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=722fafcc38eb4c41aae3b84db65b4f77')
response = requests.get(url)
print(response.json())