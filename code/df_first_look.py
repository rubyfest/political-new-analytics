import pandas as pd
import cache_saves

df = cache_saves.open_df('articles_df')
grouped_df = df.groupby('source').mean()
top_words_fox = grouped_df.T.sort_values('Fox', ascending=False).head(10)
top_words_cbs = grouped_df.T.sort_values('CBS', ascending=False).head(10)
print(top_words_fox)
print(top_words_cbs)