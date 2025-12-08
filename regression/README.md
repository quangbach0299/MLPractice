# Regression Analysis - StudentScore

This script performs regression analysis on student score data using scikit-learn.

## File Requirements

Place the `StudentScore.xls` file in this `regression/` directory.

**Note:** The script automatically handles both CSV files (with .xls extension) and genuine Excel files. It first tries to read as CSV (faster), and if that fails, reads as Excel format.

## Running the Script

The script now includes robust path resolution that works in multiple execution contexts:

### Method 1: Run as Script (PyCharm Run Button)
Simply click the Run button in PyCharm. The script will automatically detect its location.

### Method 2: Terminal from regression/ directory
```bash
cd regression
python regression.py
```

### Method 3: Terminal from project root
```bash
python regression/regression.py
```

### Method 4: Python Console (Interactive Mode)

#### Option A: Console from project root
Open Python Console in PyCharm (from project root), then execute:
```python
exec(open('regression/regression.py').read())
```
or copy-paste the code line by line.

#### Option B: Console from regression/ directory
If you want to run line-by-line in Python Console:
1. First, change to the regression directory:
```python
import os
os.chdir('regression')
```
2. Then execute the script lines or:
```python
exec(open('regression.py').read())
```

## How It Works

The script uses smart path resolution:

1. **Script Mode** (when `__file__` is defined): Uses the script's directory location
2. **Console Mode** (when `__file__` is not defined): 
   - First checks current directory for `StudentScore.xls`
   - Then checks `regression/` subdirectory (if running from project root)
   - Falls back to constructing the path from current working directory

This ensures the script works reliably regardless of how you execute it!

## Notes

- The data file `StudentScore.xls` is gitignored and must be provided separately
- Make sure pandas and scikit-learn are installed: `pip install pandas scikit-learn ydata-profiling`
- For Excel file support, also install: `pip install openpyxl xlrd`
