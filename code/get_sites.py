import requests
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import CountVectorizer
import os
import pickle
import get_site
import cache_saves

fox_political_url='https://www.foxnews.com/politics'
fox_urls=get_site.get_fox_articles(fox_political_url)
cbs_political_url='https://www.cbsnews.com/feature/election-2024/2/'
cbs_urls=get_site.get_cbs_articles(cbs_political_url)

print('Length of fox and cbs urls, respectively before opening cache:',len(fox_urls),len(cbs_urls))

fox_old_urls=cache_saves.open_list('fox_urls')
cbs_old_urls=cache_saves.open_list('cbs_urls')
fox_urls=fox_old_urls+fox_urls
fox_urls=list(set(fox_urls))
cbs_urls=cbs_old_urls+cbs_urls
cbs_urls=list(set(cbs_urls))

fox_articles=[]
cbs_articles=[]
fox_sites=[]
cbs_sites=[]

for url in fox_urls:
    if get_site.get_fox_site(url) != None:
        fox_articles.append(get_site.get_fox_site(url))
        fox_sites.append(url)
for url in cbs_urls:
    if get_site.get_cbs_site(url) != None:
        cbs_articles.append(get_site.get_cbs_site(url))
        cbs_sites.append(url)

fox_urls=fox_sites
cbs_urls=cbs_sites

print('Length of fox and cbs urls, respectively after opening cache:',len(fox_urls),len(cbs_urls))

cache_saves.save_list(fox_urls, 'fox_urls')
cache_saves.save_list(cbs_urls, 'cbs_urls')













'''
# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the title
    title = soup.find('h1').get_text()

    # Extract the article content
    content = []
    for paragraph in soup.find_all('p'):
        content.append(paragraph.get_text())
    
    # Join the content into a single string
    article_content = '\n'.join(content)

    # Output the results
    #print(f'Title: {title}')
    #print('Content:')
    #print(article_content)
else:
    print(f'Failed to retrieve the article. Status code: {response.status_code}')



texts = [article_content]

# Create a CountVectorizer instance
vectorizer = CountVectorizer()

# Fit and transform the text data
X = vectorizer.fit_transform(texts)

# Convert the result to an array
vectorized_text = X.toarray()

# Display the vectorized representation
print("Vocabulary:", vectorizer.get_feature_names_out())
print("Vectorized Text:\n", vectorized_text)
'''