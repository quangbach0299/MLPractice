import sklearn
import pandas as pd
from sklearn.model_selection import train_test_split

# from ydata_profiling import ProfileReport

data = pd.read_csv("diabetes.csv")  # Hiện tại

# profile = ProfileReport(data, title="Diabetes Data Profiling Report")
# profile.to_file("diabetes_data_profile.html")
target = "Outcome"
x = data.drop(target, axis=1)
# print(x.head())
y = data[target]
# print(y.head())

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state= 1402)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)