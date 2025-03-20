# Module Import Guide

## 1. Fixing Circular Import Problem
### Problem:
Circular imports occur when two modules depend on each other directly, causing Python to get stuck in an infinite loop while loading them.

### Solution:
To fix this, we use **lazy imports**, moving the import statement inside the function that requires it. This prevents Python from trying to load both modules simultaneously.

#### Example:
```python
# module_a.py

def func_a():
    return "Function A"

def call_func_b():
    from module_b import func_b  # Lazy import
    return func_b()

print(call_func_b())
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
### Task:
Write a program that dynamically imports and executes a function from any module specified by the user.

### Solution:
We use **importlib** to import the module at runtime and retrieve the function dynamically.

#### Example:
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

module_name = input("Enter module name: ")
function_name = input("Enter function name: ")
argument = float(input("Enter argument: "))
dynamic_import_and_execute(module_name, function_name, argument)
```

---

## 3. Custom Module with Exception Handling
### Task:
Create a `calculator.py` module that handles division errors gracefully.

### Solution:
Use **try-except blocks** to catch division by zero and other errors.

#### Example:
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
#### Usage:
```python
from calculator import divide
print(divide(10, 2))  # Output: 5.0
print(divide(10, 0))  # Output: Cannot divide by zero.
```

---

## 4. Advanced Import Strategies
### Task:
Check if a function exists in a module before executing it.

### Solution:
Use **hasattr()** to check if the function is present before calling it.

#### Example:
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
#### Usage:
```python
safe_import_and_execute("math", "sqrt", 25)  # Output: 5.0
```

---

## 5. Optimizing Import Time
### Task:
Measure the time taken to import modules.

### Solution:
Use the **time** module to compare single imports vs. importing everything.

#### Example:
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

## 6. Module Creation and Distribution
### Task:
Create a Python package and make it installable using `setup.py`.

### Solution:
1. **Create a package structure:**
```
my_package/
    ├── my_package/
    │   ├── __init__.py
    │   ├── module_x.py
    ├── setup.py
```
2. **Write `setup.py`**
```python
from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
)
```
3. **Install the package locally:**
```sh
pip install .
```
4. **Test the package:**
```python
from my_package import module_x
print(module_x.some_function())
```

---

## 7. Investigating sys.path
### Task:
Modify `sys.path` to import modules from a custom directory.

### Solution:
Use **sys.path.append()** to add the directory dynamically.

#### Example:
```python
import sys
sys.path.append("/custom/path/to/modules")
import mymodule  # Now this will work if `mymodule.py` exists in that path
```
