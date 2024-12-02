import pandas as pd
import cache_saves
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

df = cache_saves.open_df('articles_df')
df=df.drop(columns=['brennan','margaret','cbs','fox', 'report'])
df=df.drop(columns=['source'])
df = df.loc[:, df.sum() >= 20]
df['source'] = cache_saves.open_list('articles_df')['source']
grouped_df = df.groupby('source').mean()
#creates a list of columns in grouped df where one source has a count of 0
zero_columns = []

# Iterate through the columns
for col in grouped_df.columns:
    if (grouped_df[col] == 0).any():  # Check if either row has a 0
        zero_columns.append(col)
#drops those columns in df
df = df.drop(columns=zero_columns)
#drops those columns in grouped df
grouped_df = df.groupby('source').mean()
top_words_fox = grouped_df.T.sort_values('Fox', ascending=False)
top_words_cbs = grouped_df.T.sort_values('CBS', ascending=False)

# Calculate row-wise total word counts
row_sums = df.drop(columns=['source']).sum(axis=1)
# Convert counts to proportions
proportion_df = df.drop(columns=['source']).div(row_sums, axis=0)
# Add back the source column
proportion_df['source'] = df['source']
# Group by source and calculate the mean proportions
grouped_proportion_df = proportion_df.groupby('source').mean()
# Sort the proportions by source
top_words_fox_proportion = grouped_proportion_df.T.sort_values('Fox', ascending=False)
top_words_cbs_proportion = grouped_proportion_df.T.sort_values('CBS', ascending=False)

#compares when words are used significantly more in one source than the other
prop_diff = grouped_proportion_df.div(grouped_proportion_df.sum(axis=0), axis=1)
top_prop_diff_fox = prop_diff.T.sort_values('Fox', ascending=False)
top_prop_diff_cbs = prop_diff.T.sort_values('CBS', ascending=False)

#saving dfs to cache
cache_saves.save_df(top_words_fox, 'top_words_fox')
cache_saves.save_df(top_words_cbs, 'top_words_cbs')
cache_saves.save_df(top_words_fox_proportion, 'top_words_fox_proportion')
cache_saves.save_df(top_words_cbs_proportion, 'top_words_cbs_proportion')
cache_saves.save_df(top_prop_diff_fox, 'top_prop_diff_fox')
cache_saves.save_df(top_prop_diff_cbs, 'top_prop_diff_cbs')
cache_saves.save_df(df, 'filtered_final_df')
