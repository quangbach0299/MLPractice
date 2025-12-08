import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from ydata_profiling import ProfileReport


data = pd.read_csv('StudentScore.xls')

# profile = ProfileReport(x_train, title="Student Score Report")
# profile.to_file("student_score_profiling_report.html")
 
print(data[["reading score","writing score","math score"]].corr()) # Bảng này dùng để xem mối tương quan giữa các biến với nhau

# Dữ liệu có độ tuyến tính cao thì ta sẽ sử dụng modal hồi tuyến tính để dự đoán: Linear Regression Model
target = "math score"
x = data.drop(target, axis=1)
y = data[target]

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=1009
)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)



 