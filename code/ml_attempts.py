import sklearn
import pandas as pd
import cache_saves
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict, StratifiedKFold
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn import tree
from sklearn import metrics
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.neighbors import KNeighborsClassifier

df = cache_saves.open_df('filtered_final_df')
y=df['source']
X=df.drop(columns=['source'])
y_train, y_test, X_train, X_test = train_test_split(y, X, test_size=0.4, random_state=42)
tree_clf=DecisionTreeClassifier(random_state=42)
tree_clf.fit(X_train, y_train)
y_pred=tree_clf.predict(X_test)
report=classification_report(y_test, y_pred)
print(report)

pred = cross_val_predict(estimator=tree_clf, X=X, y=y, cv=50)
report = classification_report(y, pred)
print(report)

forest_clf = RandomForestClassifier(random_state=42)
forest_clf.fit(X_train, y_train)
y_pred = forest_clf.predict(X_test)
report = classification_report(y_test, y_pred)
print(report)

pred = cross_val_predict(estimator=forest_clf, X=X, y=y, cv=50)
report = classification_report(y, pred)
print(report)