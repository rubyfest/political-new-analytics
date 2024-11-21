import playwright_get_site
import cache_saves
import pandas as pd
from playwright.sync_api import sync_playwright

fox_urls = cache_saves.open_list('fox_urls')
with sync_playwright() as playwright:
    print('Length of fox urls:', len(fox_urls))
    for url in fox_urls:
        print(url)
        print(playwright_get_site.get_fox_site(playwright, url)[0:10])
        print('\n\n')
    cbs_urls = cache_saves.open_list('cbs_urls')
    print('Length of cbs urls:', len(cbs_urls))