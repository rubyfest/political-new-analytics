import sklearn
import pandas as pd
import cache_saves
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict, StratifiedKFold, GridSearchCV
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
'''
classifier = RandomForestClassifier(random_state=42)


# Define parameter grid
param_grid = {
    'n_estimators': [50, 100, 200, None],
    'max_depth': [None, 5, 10, 20],
    'min_samples_split': [2, 5, 10, None],
    'min_samples_leaf': [1, 2, 4, None],
}

grid_search = GridSearchCV(classifier, param_grid, cv=5, scoring='f1_macro')
grid_search.fit(X, y)
print("Best Parameters:", grid_search.best_params_)
print("Best Score:", grid_search.best_score_)
'''

final_forest_clf = RandomForestClassifier(n_estimators=100, max_depth=10, min_samples_split=5, min_samples_leaf=2, random_state=42)
pred = cross_val_predict(estimator=forest_clf, X=X, y=y, cv=5)
report = classification_report(y, pred)
print(report)

gb_clf = GradientBoostingClassifier(random_state=42)
gb_clf.fit(X_train, y_train)
y_pred = gb_clf.predict(X_test)
report = classification_report(y_test, y_pred)
print(report)

pred = cross_val_predict(estimator=gb_clf, X=X, y=y, cv=5)
report = classification_report(y, pred)
print(report)

classifier=GradientBoostingClassifier(random_state=42)
'''
# Define parameter grid
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 10],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
}

grid_search = GridSearchCV(classifier, param_grid, cv=5, scoring='f1_macro')
grid_search.fit(X, y)
print("Best Parameters:", grid_search.best_params_)
print("Best Score:", grid_search.best_score_)
'''

final_gb_clf = GradientBoostingClassifier(n_estimators=50, max_depth=3, min_samples_split=5, min_samples_leaf=1, random_state=42)
pred = cross_val_predict(estimator=final_gb_clf, X=X, y=y, cv=5)
report = classification_report(y, pred)
print(report)