import get_sites
import cache_saves
import pandas as pd

fox_urls = cache_saves.open_list('fox_urls')
print('Length of fox urls before opening cache:', len(fox_urls))