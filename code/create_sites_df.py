import playwright_get_site
import cache_saves
import pandas as pd
from playwright.sync_api import sync_playwright
from sklearn.feature_extraction.text import CountVectorizer

with sync_playwright() as playwright:
    fox_articles = []
    cbs_articles = []
    fox_urls = cache_saves.open_list('fox_urls_new')
    print('Length of fox urls:', len(fox_urls))
    for url in fox_urls:
        fox_articles.append(playwright_get_site.get_fox_site(playwright, url))
        #print(url)
        #print(playwright_get_site.get_fox_site(playwright, url)[0:10])
        #print('\n\n')

    cbs_urls = cache_saves.open_list('cbs_urls_new')
    print('Length of cbs urls:', len(cbs_urls))
    for url in cbs_urls:
        cbs_articles.append(playwright_get_site.get_cbs_site(playwright, url))
    #    print(url)
    #    print(playwright_get_site.get_cbs_site(playwright, url)[0:10])
    #    print('\n\n')
#print(fox_articles, cbs_articles)

articles=cbs_articles+fox_articles
sources = ["CBS"] * len(cbs_articles) + ["Fox"] * len(fox_articles)

# Create a combined dataset with source labels
articles = cbs_articles + fox_articles
sources = ["CBS"] * len(cbs_articles) + ["Fox"] * len(fox_articles)

# Initialize the CountVectorizer
vectorizer = CountVectorizer()

# Transform the articles into a word count matrix
word_count_matrix = vectorizer.fit_transform(articles)

# Convert the matrix to a DataFrame
df = pd.DataFrame(
    word_count_matrix.toarray(), 
    columns=vectorizer.get_feature_names_out()
)

# Add the source column
df['source'] = sources

# Display the DataFrame
print(df)

# Save the DataFrame to a cache file
cache_saves.save_df(df, 'articles_df')
