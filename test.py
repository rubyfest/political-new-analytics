import requests
from bs4 import BeautifulSoup
from datetime import datetime
'''
url='https://www.foxnews.com/politics/trump-taps-former-acting-ag-matthew-whitaker-nato-ambassador'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    date = soup.find('time').get_text()
    date = date[:date.find(' EST')].strip()
    date=datetime.strptime(date, "%B %d, %Y %I:%M%p")
    print(date)
'''

a='NATIONAL POLLS SHOW TRUMP, HARRIS IN TIGHT RACE AS ELECTORATE IS UNHAPPY WITH CHOICES'
b='NATIONAL POLLS SHOW TRUMP, HARRIS IN TIGHT RACE AS ELECTORATE IS UNHAPPY WITH CHOICES'
if a == b:
    print('yes')