import pandas as pd
import sklearn.model_selection as train_test_split

data = pd.read_csv("csgo.csv")
target = "result"
x = data.drop(target, axis=1)
y = data[target]
print(x.head())
print(y.head())