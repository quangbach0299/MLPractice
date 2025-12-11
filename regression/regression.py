import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.linear_model import LinearRegression
from ydata_profiling import ProfileReport
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

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

# Numerical là dữ liệu số
# Chẳng hạn như: điểm số, chiều cao, cân nặng
num_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
])

# Nomial là dữ liệu phân loại không có thứ tự
# Chẳng hạn như: giới tính, chủng tộc
nom_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(sparse_output=False))
])
# Ordinal là dữ liệu phân loại có thứ tự
# Chẳng hạn như: thấp, trung bình, cao
# Sắp xếp từ trình độ giáo dục thấp đến cao
education_values = [
    "some high school",
    "high school",
    "some college",
    "associate's degree",
    "bachelor's degree",
    "master's degree"
]
gender_values = x_train["gender"].unique()
lunch_values = x_train["lunch"].unique()
test_prep_values = x_train["test preparation course"].unique()
ord_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OrdinalEncoder(categories=[
        education_values,
        gender_values,
        lunch_values,
        test_prep_values
    ]))
])

preprocessor = ColumnTransformer(transformers=[("num_features", num_transformer, ["reading score", "writing score"]),
                                               ("nom_features", nom_transformer, ["race/ethnicity"]),
                                               ("ord_features", ord_transformer, ["parental level of education", "gender", "lunch", "test preparation course"])
                                               ])   

result = preprocessor.fit_transform(x_train)
# print(result)

# Build Linear Regression model with preprocessing
models = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])

fitted_models = models.fit(x_train, y_train)

y_predict = models.predict(x_test)

mae = mean_absolute_error(y_test, y_predict)
mse = mean_squared_error(y_test, y_predict)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_predict)


print("LINEAR REGRESSION RESULTS")
print("MAE:", format(mae))
print("MSE:", format(mse))
print("RMSE:", format(rmse))
print("R2:", format(r2))

# Impute missing values 
# imputer = SimpleImputer(strategy='median')
# x_train["reading score"]= imputer.fit_transform(x_train[["reading score"]])
# x_test["reading score"] =  imputer.transform(x_test[["reading score"]])
#
# scaler = StandardScaler()
# x_train["reading score"] = scaler.fit_transform(x_train[["reading score"]])
# x_test["reading score"] = scaler.transform(x_test[["reading score"]])


# In ra muc do anh huong cua các features tới output
# feature_names = models["preprocessor"].get_feature_names_out()
# coefficients = models["regressor"].coef_
# print("Feature Importance:")
# for name, coef in zip(feature_names, coefficients):
#     print(f"{name}: {coef}")    