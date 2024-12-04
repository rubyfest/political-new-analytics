import pandas as pd
import cache_saves
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import classification_report
from sklearn.ensemble import GradientBoostingClassifier

# Load data
top_words_fox = cache_saves.open_df('top_words_fox')
top_words_cbs = cache_saves.open_df('top_words_cbs')
top_words_fox_proportion = cache_saves.open_df('top_words_fox_proportion')
top_words_cbs_proportion = cache_saves.open_df('top_words_cbs_proportion')
top_prop_diff_fox = cache_saves.open_df('top_prop_diff_fox')
top_prop_diff_cbs = cache_saves.open_df('top_prop_diff_cbs')
df=cache_saves.open_df('filtered_final_df')


st.title('Comparing Language in Fox and CBS Election Articles')
st.caption('This app compares the language used in election articles from Fox News and CBS News. The goal is to see specific words used more frequently in one source than the other.')
st.caption('Fox is known to be more :conservative, while CBS is known to be more liberal. Although there is not enough data or source companies to generalize how a left leaning or right leaning source differs in language, this app will show the differences between Fox and CBS, looking at over 50 articles of each.')
st.subheader(':grey[Count of top words:]',divider='grey')
col1, col2 = st.columns(2)
col1.caption(':red[FOX]')
col1.dataframe(top_words_fox)
col2.caption(':blue[CBS]')
col2.dataframe(top_words_cbs)
st.subheader(':grey[Proportion of top words:]',divider='grey')
col1, col2 = st.columns(2)
col1.write(':red[FOX]')
col1.dataframe(top_words_fox_proportion)
col2.write(':blue[CBS]')
col2.dataframe(top_words_cbs_proportion)
st.subheader(':grey[Top proportion difference of words:]',divider='grey')
col1, col2 = st.columns(2)
col1.write(':red[FOX]')
col1.dataframe(top_prop_diff_fox)
col2.write(':blue[CBS]')
col2.dataframe(top_prop_diff_cbs)

word_search=st.text_input(':violet[Type a word to find how it compares in FOX and CBS articles:]')
if word_search:
    word_search=word_search.lower()
    st.subheader(f':grey[Word Search for "{word_search}":]',divider='grey')
    col1, col2 = st.columns(2)
    if word_search in df.columns:
        searched_df=df[[word_search, 'source']]
        searched_df=searched_df.rename(columns={word_search: 'word count'})
        searched_df=searched_df.sort_values('word count', ascending=False)
        col1.dataframe(searched_df)
        word_counts=round(top_words_fox.loc[word_search, 'Fox'],4), round(top_words_cbs.loc[word_search, 'CBS'],4)
        word_proportions=round(top_words_fox_proportion.loc[word_search, 'Fox'],6), round(top_words_cbs_proportion.loc[word_search, 'CBS'],6)
        word_prop_diff=round(top_prop_diff_fox.loc[word_search, 'Fox'],4), round(top_prop_diff_cbs.loc[word_search, 'CBS'],4)
        col2.write(':violet[Average Word Counts:]')
        col2.write(f':red[Fox]: {word_counts[0]}')
        col2.write(f':blue[CBS]: {word_counts[1]}')
        col2.write(':violet[Average Word Proportions:]')
        col2.write(f':red[Fox]: {word_proportions[0]}')
        col2.write(f':blue[CBS]: {word_proportions[1]}')
        col2.write(':violet[Word Proportion Difference:]')
        col2.write(f':red[Fox]: {word_prop_diff[0]}')
        col2.write(f':blue[CBS]: {word_prop_diff[1]}')

    else:
        st.write(f'The word "{word_search}" is not in the top words for Fox or CBS articles.')

st.title('Visualizations')
colors=['blue','red']
st.caption(':violet[Hover over a plot and click the arrow icon to expand it]')
st.subheader(":grey[Plots of top word counts on average:]",divider='grey')
col1, col2 = st.columns(2)
col1.write(':red[FOX]')
figure, series1 = plt.subplots()
top_words_fox.head(10).plot(kind='bar', ax=series1, figsize=(10, 6), color=colors)
series1.set_title('Top words for Fox News by Count')
series1.set_ylabel('Word Count')
series1.set_xlabel('Word')
series1.set_xticklabels(series1.get_xticklabels(), rotation=45)
series1.legend(title='Source', fontsize=12)
col1.pyplot(figure)

col2.write(':blue[CBS]')
figure2, series2 = plt.subplots()
top_words_cbs.head(10).plot(kind='bar', ax=series2, figsize=(10, 6), color=colors)
series2.set_title('Top words for CBS News by Count')
series2.set_ylabel('Word Count')
series2.set_xlabel('Word')
series2.set_xticklabels(series2.get_xticklabels(), rotation=45)
series2.legend(title='Source', fontsize=12)
col2.pyplot(figure2)

st.subheader(":grey[Plots of top word proportions on average:]",divider='grey')
col1, col2 = st.columns(2)
col1.write(':red[FOX]')
figure3, series3 = plt.subplots()
top_words_fox_proportion.head(10).plot(kind='bar', ax=series3, figsize=(10, 6), color=colors)
series3.set_title('Top words for Fox News by Proportion')
series3.set_ylabel('Word Proportion')
series3.set_xlabel('Word')
series3.set_xticklabels(series3.get_xticklabels(), rotation=45)
series3.legend(title='Source', fontsize=12)
col1.pyplot(figure3)

col2.write(':blue[CBS]')
figure4, series4 = plt.subplots()
top_words_cbs_proportion.head(10).plot(kind='bar', ax=series4, figsize=(10, 6), color=colors)
series4.set_title('Top words for CBS News by Proportion')
series4.set_ylabel('Word Proportion')
series4.set_xlabel('Word')
series4.set_xticklabels(series4.get_xticklabels(), rotation=45)
series4.legend(title='Source', fontsize=12)
col2.pyplot(figure4)

st.subheader(":grey[Plots of top proportion difference of words:]",divider='grey')
col1, col2 = st.columns(2)
col1.write(':red[FOX]')
figure5, series5 = plt.subplots()
top_prop_diff_fox.head(10).plot(kind='bar', ax=series5, figsize=(10, 6), color=colors)
series5.set_title('Top proportion difference of words for Fox News')
series5.set_ylabel('Proportion Difference')
series5.set_xlabel('Word')
series5.set_xticklabels(series5.get_xticklabels(), rotation=45)
series5.legend(title='Source', fontsize=12)
col1.pyplot(figure5)

col2.write(':blue[CBS]')
figure6, series6 = plt.subplots()
top_prop_diff_cbs.head(10).plot(kind='bar', ax=series6, figsize=(10, 6), color=colors)
series6.set_title('Top proportion difference of words for CBS News')
series6.set_ylabel('Proportion Difference')
series6.set_xlabel('Word')
series6.set_xticklabels(series6.get_xticklabels(), rotation=45)
series6.legend(title='Source', fontsize=12)
col2.pyplot(figure6)

st.title('Gradient Boosting Classifier')
st.caption('Having tested different machine learning algorithms (decision tree, random forest, gradient boosting), the Gradient Boosting Classifier seen below is the top scoring model.')
y=df['source']
X=df.drop(columns=['source'])

st.subheader(':grey[Algorithm Arguments:]')
st.write(':violet[n_estimators: 50]')
st.write(':violet[max_depth: 3]')
st.write(':violet[min_samples_split: 5]')
st.write(':violet[min_samples_leaf: 1]')
st.write(':violet[random_state: 42]')

final_gb_clf = GradientBoostingClassifier(n_estimators=50, max_depth=3, min_samples_split=5, min_samples_leaf=1, random_state=42)
pred = cross_val_predict(estimator=final_gb_clf, X=X, y=y, cv=5)
report = classification_report(y, pred, output_dict=True)
report = pd.DataFrame(report).T
st.dataframe(report)

final_gb_clf.fit(X, y)

feature_importances = final_gb_clf.feature_importances_

# Get the names of the features
feature_names = list(X.columns)

# Create a dictionary mapping feature names to importance scores
feature_importance_dict = dict(zip(feature_names, feature_importances))

# Sort the dictionary by importance score in descending order
sorted_feature_importance = sorted(feature_importance_dict.items(), key=lambda x: x[1], reverse=True)

# Select only the top 10 features
top_features = [x[0] for x in sorted_feature_importance[:10]]
top_importances = [x[1] for x in sorted_feature_importance[:10]]

# Print top 10 feature importance scores
st.subheader(":grey[Most Important Features:]")
st.caption(':violet[Permutation Importance] :grey[(How much worse the model gets with the removal of each feature)]')
feature_importance_df=pd.DataFrame(sorted_feature_importance, columns=['Feature', 'Importance'])
st.dataframe(feature_importance_df)

top_feature_importance_df = feature_importance_df.head(10)

# Plot top 10 feature importance scores
figure7, series7 = plt.subplots()
top_feature_importance_df.plot(ax=series7, figsize=(10, 6), x='Feature', y='Importance', kind='barh', color='purple')   
series7.set_xlabel('Feature Importance')
series7.set_ylabel('Feature')
series7.set_title('Top 10 Most Important Features in Gradient Boosting')
st.pyplot(figure7)