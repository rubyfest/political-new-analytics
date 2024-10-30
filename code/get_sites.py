import requests
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import CountVectorizer
import get_site

fox_political_url='https://www.foxnews.com/politics'
fox_urls=get_site.get_fox_articles(fox_political_url)
cbs_political_url='https://www.cbsnews.com/feature/election-2024/2/'
cbs_urls=get_site.get_cbs_articles(cbs_political_url)

fox_articles=[]
cbs_articles=[]
for url in fox_urls:
    if get_site.get_fox_site(url) != None:
        fox_articles.append(get_site.get_fox_site(url))
for url in cbs_urls:
    if get_site.get_cbs_site(url) != None:
        cbs_articles.append(get_site.get_cbs_site(url))
print(len(fox_articles))
print(len(cbs_articles))
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