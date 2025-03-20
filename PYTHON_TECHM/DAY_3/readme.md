# Python Modules and Import Strategies

## 1. Fixing Circular Import Issue

### **Problem:**
Circular imports occur when two modules depend on each other, causing Python to get stuck in a loop and raise an `ImportError`.

### **Solution:**
- Use **lazy imports** by placing the `import` statements inside functions instead of at the top of the module.
- Example:
  ```python
  # module_a.py
  def func_a():
      return "Function A"

  def call_func_b():
      from module_b import func_b  # Lazy import
      return func_b()
  ```
  ```python
  # module_b.py
  def func_b():
      return "Function B"

  def call_func_a():
      from module_a import func_a  # Lazy import
      return func_a()
  ```

---

## 2. Dynamic Module Loading

### **Problem:**
We need to dynamically import a module and execute a function specified by the user.

### **Solution:**
- Use `importlib.import_module()` to load the module at runtime.
- Use `getattr()` to access the function and execute it with user-provided arguments.
- Example:
  ```python
  import importlib

  def dynamic_import_and_execute(module_name, function_name, argument):
      try:
          module = importlib.import_module(module_name)
          func = getattr(module, function_name)
          result = func(argument)
          print(f"Output: {result}")
      except (ModuleNotFoundError, AttributeError, TypeError) as e:
          print(f"Error: {e}")
  ```

---

## 3. Custom Module with Exception Handling

### **Problem:**
Create a module (`calculator.py`) that handles division by zero and invalid inputs gracefully.

### **Solution:**
- Use `try-except` blocks to catch `ZeroDivisionError` and other exceptions.
- Example:
  ```python
  # calculator.py
  def divide(a, b):
      try:
          return a / b
      except ZeroDivisionError:
          return "Cannot divide by zero."
      except Exception as e:
          return f"Error: {e}"
  ```
  ```python
  # Importing and using calculator.py
  from calculator import divide
  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))
  print("Result:", divide(num1, num2))
  ```

---

## 4. Advanced Import Strategies

### **Problem:**
Check if a function exists in a module before executing it to avoid runtime errors.

### **Solution:**
- Use `importlib.import_module()` to import the module.
- Use `hasattr()` to check if the function exists before calling it.
- Example:
  ```python
  import importlib

  def safe_import_and_execute(module_name, function_name, *args):
      try:
          module = importlib.import_module(module_name)
          if hasattr(module, function_name):
              func = getattr(module, function_name)
              result = func(*args)
              print(f"Output: {result}")
          else:
              print(f"Error: Function '{function_name}' not found in module '{module_name}'.")
      except ModuleNotFoundError:
          print(f"Error: Module '{module_name}' not found.")
      except Exception as e:
          print(f"Unexpected error: {e}")
  ```

---

## 5. Optimizing Import Time

### **Problem:**
Measure the import time of different import methods.

### **Solution:**
- Use the `time` module to track the execution time of different import methods.
- Example:
  ```python
  import time

  start = time.time()
  import math
  end = time.time()
  print(f"Single import time: {end - start:.6f} seconds")

  start = time.time()
  from math import *
  end = time.time()
  print(f"Import everything time: {end - start:.6f} seconds")
  ```

---

## 6. Investigating `sys.path`

### **Problem:**
Explore `sys.path` and add a custom directory to import modules from an unconventional path.

### **Solution:**
- Print the default `sys.path` to check where Python looks for modules.
- Append a custom directory dynamically using `sys.path.append()`.
- Example:
  ```python
  import sys

  print("Default sys.path:")
  for path in sys.path:
      print(path)

  # Add a custom module path
  custom_path = r"C:\\Users\\Abhis\\custom_modules"
  sys.path.append(custom_path)

  try:
      import mymodule  # Custom module
      print("Module imported successfully!")
  except ModuleNotFoundError:
      print("Module not found in the specified path.")
  ```

**Alternative: Permanent Solution**
- Set `PYTHONPATH` environment variable so Python always recognizes the custom directory.
  - **Windows (CMD):**
    ```sh
    set PYTHONPATH=C:\Users\Abhis\custom_modules;%PYTHONPATH%
    ```
  - **macOS/Linux:**
    ```sh
    export PYTHONPATH=/home/user/custom_modules:$PYTHONPATH
    ```

---

### **Summary:**
Each of these problems involves handling module imports efficiently while avoiding common issues like circular dependencies, missing functions, and slow imports. Using techniques such as `importlib`, `sys.path`, and exception handling makes Python programs more modular and error-resilient.

---

**Author:** Abhishek Yadav  
**Date:** March 20, 2025