import sys

custom_path = r"C:\Users\Abhis\Desktop\PYTHON_TRAINING\PYTHON_TECHM\DAY_3\modules_assignment\my_package"  # Update with your actual path
sys.path.append(custom_path)  # Add the custom path

try:
    import my_package  # Try importing the module from the custom path
    print("Module imported successfully!")
except ModuleNotFoundError:
    print("Module not found in the specified path.")
