from playwright.sync_api import Playwright, sync_playwright, expect
import streamlit as st
import pandas as pd

def get_fox_site(playwright: Playwright, url: str) -> str:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(200000)
    page.goto(url)
    page.wait_for_selector('div.article-body')
    article = page.query_selector('div.article-body')
    article_text = article.query_selector_all('p')
    links = article.query_selector_all('strong')
    link_count=0
    link_text=[]
    for link in links:
        link_text.append(link.inner_text().strip())
    article=[]
    #print('text' , len(link_text))
    #print(link_text)
    for paragraph in article_text[1:-1]:
        text=paragraph.inner_text().strip()
        #print(text)
        #print(link_text[link_count])
        if link_text[link_count] == '\xa0' and link_count < len(link_text)-1:
            link_count+=1
            #print('added')
        if link_text[link_count] in text:
            if link_text[link_count] == text:
                if 'CLICK HERE TO GET THE FOX NEWS APP' in text:
                    pass
                    #print('done')
                elif link_count == len(link_text)-1:
                    pass
                    #print(link_count)
                else:
                    #print('link count:',link_count+1,text)
                    #print(link_count)
                    link_count+=1
            else:
                if 'CLICK HERE TO GET THE FOX NEWS APP' in text:
                    text=text.replace('CLICK HERE TO GET THE FOX NEWS APP','')
                    #print('done')
                elif link_count == len(link_text)-1:
                    text=text.replace(link_text[link_count],'')
                    #print(link_count)
                else:
                    #print('link count:',link_count+1,text)
                    #print(link_count)
                    text=text.replace(link_text[link_count],'')
                    link_count+=1
                article.append(text)
        else:
            article.append(text)
        #print(text)
    context.close()
    browser.close()
    return ' '.join(article)

    # ---------------------


def get_cbs_site(playwright: Playwright, url: str) -> str:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url)
    page.wait_for_selector('section.content__body')
    article = page.query_selector('section.content__body')
    article_text = article.query_selector_all('p')
    article=[]
    for paragraph in article_text[0:]:
        text=paragraph.inner_text().strip()
        article.append(text)
    context.close()
    browser.close()
    return ' '.join(article)

    # ---------------------

if __name__ == '__main__':
    fox_url = 'https://www.foxnews.com/politics/trump-taps-former-acting-ag-matthew-whitaker-nato-ambassador'
    cbs_url = 'https://www.cbsnews.com/news/kamala-harris-fundraising-campaign-appeals/'
    with sync_playwright() as playwright:
        article=get_fox_site(playwright, url=fox_url)
        print(article)
        print('\n\n')
        article=get_cbs_site(playwright, url=cbs_url)
        print(article)