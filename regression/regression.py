import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from ydata_profiling import ProfileReport
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

# Xử lý đường dẫn cho cả Run và Console
current_dir = os.path.dirname(os.path.realpath(__file__)) if '__file__' in globals() else os.path.join(os.getcwd(), "regression") if not os.path.exists("StudentScore.xls") else os.getcwd()
data = pd.read_csv(os.path.join(current_dir, "StudentScore.xls"))

# profile = ProfileReport(x_train, title="Student Score Report")
# profile.to_file("student_score_profiling_report.html")
 
# print(data[["reading score","writing score","math score"]].corr()) # Bảng này dùng để xem mối tương quan giữa các biến với nhau

# Dữ liệu có độ tuyến tính cao thì ta sẽ sử dụng modal hồi tuyến tính để dự đoán: Linear Regression Model
target = "math score"
x = data.drop(target, axis=1)
y = data[target]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1009)

nums_transformer = Pipeline(steps=[("imputer", SimpleImputer(strategy="median")),
                                   ("scaler", StandardScaler())])


result = nums_transformer.fit_transform(x_train[["reading score", "writing score"]])
for i,j in zip(x_train[["reading score", "writing score"]].values, result):
    print("Before:{}. After:{}".format(i,j))


# Impute missing values
# imputer = SimpleImputer(strategy='median')
# x_train["reading score"]= imputer.fit_transform(x_train[["reading score"]])
# x_test["reading score"] =  imputer.transform(x_test[["reading score"]])
#
# scaler = StandardScaler()
# x_train["reading score"] = scaler.fit_transform(x_train[["reading score"]])
# x_test["reading score"] = scaler.transform(x_test[["reading score"]])