import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
import pickle
from lazypredict.Supervised import LazyClassifier


# Load data
data = pd.read_csv("diabetes.csv")

# Prepare data
target = "Outcome"
x = data.drop(target, axis=1)
y = data[target]

# Split data
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=1009
)

# Scale features
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

## Train model
# param_grid = {
#     'n_estimators': [50, 100, 200, 150],
#     'criterion': ['gini', 'entropy', 'log_loss'],
#     # 'max_depth': [None, 2, 5, 10],
# }

# model = RandomForestClassifier(random_state=100)
# model = GridSearchCV(
#     estimator=RandomForestClassifier(random_state=100),
#     param_grid=param_grid,
#     scoring='recall',
#     cv=6,
#     verbose=2,
#     n_jobs=4
# )

clf = LazyClassifier(verbose=0, ignore_warnings=True, custom_metric=None)
models, predictions = clf.fit(x_train, x_test, y_train, y_test) 
print(models)


# model.fit(x_train, y_train)
# print("Best score: ", model.best_score_)
# print("Best Parameters: ", model.best_params_)
#save the model
# pickle.dump([model, scaler], open("rf_model.pkl", "wb"))

## Predict
# y_pred = model.predict(x_test)
# print(y_pred)
# print(classification_report(y_test, y_pred))

## Evaluate
# print("Accuracy:  {:.4f}".format(accuracy_score(y_test, y_pred)))
# print("Precision: {:.4f}".format(precision_score(y_test, y_pred)))
# print("Recall:    {:.4f}".format(recall_score(y_test, y_pred)))
# print("F1 Score:  {:.4f}".format(f1_score(y_test, y_pred)))