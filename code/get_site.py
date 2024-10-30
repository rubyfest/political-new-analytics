import requests
from bs4 import BeautifulSoup

def check_keywords(article_content):
    keywords = ["trump", "harris"]
    # Check if all keywords are present
    all_present = all(word.lower() in article_content.lower() for word in keywords)
    return all_present

def get_fox_site(url: str):
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
        full_text = '\n'.join(content)

        start_index = full_text.find("Refinitiv Lipper.") + len("Refinitiv Lipper.")
        end_index = full_text.find("By entering your email and clicking")

        # Extract the specific section of the text
        if start_index != -1 and end_index != -1:
            specific_content = full_text[start_index:end_index].strip()
            if check_keywords(specific_content):
                return specific_content
            else:
                pass
        else:
            pass
    else:
        pass
    
def get_cbs_site(url: str):
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
        full_text = '\n'.join(content)
    
        start_index = full_text.find("Watch CBS News") + len("Watch CBS News")
        end_index = full_text.find("2024 CBS Interactive")

        # Extract the specific section of the text
        if start_index != -1 and end_index != -1:
            specific_content = full_text[start_index:end_index].strip()
            if check_keywords(specific_content):
                return specific_content
            else:
                pass
        else:
            pass
    else:
        pass
    
def get_fox_articles(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all article links
        links = []
        for article in soup.find_all('article'):
            # Find the anchor tag with the article link
            a_tag = article.find('a')
            if a_tag and 'href' in a_tag.attrs:
                link = a_tag['href']
                # Make sure to include only full URLs
                if link.startswith('/'):
                    link = 'https://www.foxnews.com' + link
            if 'politics' in link and not link.startswith('https://www.foxnews.com/video'):
                links.append(link)

        # Print the extracted links
        return links
    else:
        return(f'Failed to retrieve the page. Status code: {response.status_code}')
    
def get_cbs_articles(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all article links
        links = []
        for article in soup.find_all('article'):
            # Find the anchor tag with the article link
            a_tag = article.find('a')
            if a_tag and 'href' in a_tag.attrs:
                link = a_tag['href']
                # Make sure to include only full URLs
                if link.startswith('/'):
                    link = 'https://www.cbsnews.com' + link
            links.append(link)

        # Print the extracted links
        return links
    else:
        return(f'Failed to retrieve the page. Status code: {response.status_code}')