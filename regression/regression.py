import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from ydata_profiling import ProfileReport
import os

# Robust file path resolution that works in multiple execution contexts:
# 1. Script execution (Run button / terminal): uses __file__ to get script directory
# 2. Python Console (interactive): uses current working directory + 'regression' subfolder
# 3. Console from regression/ directory: uses current working directory directly
try:
    # When running as a script, __file__ is defined
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'StudentScore.xls')
except NameError:
    # When running in Python Console, __file__ is not defined
    # Try current directory first (if console is opened in regression/ folder)
    if os.path.exists('StudentScore.xls'):
        file_path = 'StudentScore.xls'
    # Otherwise, try regression subdirectory (if console is opened in project root)
    elif os.path.exists(os.path.join('regression', 'StudentScore.xls')):
        file_path = os.path.join('regression', 'StudentScore.xls')
    else:
        # Final fallback: construct from current working directory
        file_path = os.path.join(os.getcwd(), 'regression', 'StudentScore.xls')

data = pd.read_csv(file_path)

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



 