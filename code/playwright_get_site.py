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
    link_text=[link.inner_text().strip() for link in links]
    captions=article.query_selector_all('div.caption')
    captions_text=[]
    captions_text_count=1
    for caption in captions:
        captions_text.append(caption.query_selector('p').inner_text().strip())
    #print(captions_text)
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
                #if 'CLICK HERE TO GET THE FOX NEWS APP' in text:
                #    pass
                #    #print('done')
                if link_count == len(link_text)-1:
                    pass
                    #print(link_count)
                else:
                    #print('link count:',link_count+1,text)
                    #print(link_count)
                    link_count+=1
            else:
                #if 'CLICK HERE TO GET THE FOX NEWS APP' in text:
                    #text=text.replace('CLICK HERE TO GET THE FOX NEWS APP','')
                    #print('done')
                if link_count == len(link_text)-1:
                    text=text.replace(link_text[link_count],'')
                    #print(link_count)
                else:
                    #print('link count:',link_count+1,text)
                    #print(link_count)
                    text=text.replace(link_text[link_count],'')
                    link_count+=1
                article.append(text)
        elif len(captions_text)>0 and captions_text[captions_text_count] in text:
            if captions_text[captions_text_count] == text:
                if captions_text_count == len(captions_text)-1:
                    pass
                else:
                    captions_text_count+=1
            else:
                if captions_text_count == len(captions_text)-1:
                    text=text.replace(captions_text[captions_text_count],'')
                else:
                    text=text.replace(captions_text[captions_text_count],'')
                    captions_text_count+=1
                article.append(text)
        else:
            article.append(text)
        #print(text)
    #print(' '.join(article))
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
    authors = article.query_selector_all('em')
    authors = [author.inner_text().strip() for author in authors]
    author_count=0
    try:
        author_content=article.query_selector('div.content-author__bio').query_selector('p').inner_text().strip()
    except:
        author_content='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    article=[]
    for paragraph in article_text[0:]:
        text=paragraph.inner_text().strip()
        if author_content in text:
            text=text.replace(author_content,'')
            article.append(text)
        else:
            if len(authors)>0 and authors[author_count] in text:
                if authors[author_count] == text:
                    if author_count == len(authors)-1:
                        pass
                    else:
                        author_count+=1
                else:
                    if author_count == len(authors)-1:
                        text=text.replace(authors[author_count],'')
                    else:
                        text=text.replace(authors[author_count],'')
                        author_count+=1
                    article.append(text)
            else:
                article.append(text)
    context.close()
    browser.close()
    #print(' '.join(article))
    #print(authors)
    return ' '.join(article)

    # ---------------------

if __name__ == '__main__':
    fox_url = 'https://www.foxnews.com/politics/trump-taps-former-acting-ag-matthew-whitaker-nato-ambassador'
    cbs_url = 'https://www.cbsnews.com/news/kamala-harris-fundraising-campaign-appeals/'
    with sync_playwright() as playwright:
        article=get_fox_site(playwright, url=fox_url)
        print(article)
        print('\n\n')
        #article=get_cbs_site(playwright, url=cbs_url)
        #print(article)
        #article=get_cbs_site(playwright, url='https://www.cbsnews.com/news/2-more-russian-disinformation-videos-targeting-u-s-election-circulating-online/')
        #print(article)