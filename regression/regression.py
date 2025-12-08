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
        # Could not find file - provide helpful error message
        raise FileNotFoundError(
            f"Could not find 'StudentScore.xls' file.\n"
            f"Current working directory: {os.getcwd()}\n"
            f"Searched in:\n"
            f"  - Current directory: {os.path.abspath('StudentScore.xls')}\n"
            f"  - Regression subdirectory: {os.path.abspath(os.path.join('regression', 'StudentScore.xls'))}\n"
            f"\nIf using Python Console, try:\n"
            f"  import os; os.chdir('regression')"
        )

# Read the data file - handle both CSV and Excel formats
# Some files may be named .xls but are actually CSV files
try:
    # First try reading as CSV (faster and more common)
    data = pd.read_csv(file_path)
except Exception as e:
    # If that fails, try reading as Excel file
    try:
        data = pd.read_excel(file_path)
    except Exception:
        raise FileNotFoundError(
            f"Could not read '{file_path}' as CSV or Excel file. "
            f"Please ensure the file exists and is in the correct format."
        )

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



 