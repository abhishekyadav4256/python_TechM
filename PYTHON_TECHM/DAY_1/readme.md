# Variables, Statements, and Expressions: A Learning Task

## 2.1. Introduction
### 2.1.1. Learning Goals
By the end of this task, students should be able to:
- Understand the basics of variables, expressions, and statements in Python.
- Differentiate between data types and apply type conversions.
- Properly name variables following Python conventions.
- Grasp the flow of execution through function calls and expressions.
- Update and reassign variables effectively.

### 2.1.2. Objectives
- Identify values and their data types.
- Perform operations using different operators.
- Understand function calls and their role in expressions.
- Explore Python's order of operations.
- Practice variable reassignment and updating.

---

## 2.2. Values and Data Types
### Research:
- A **value** in Python is any piece of data stored in memory that can be manipulated.
- Common data types in Python:
  - `int`: Integer numbers (e.g., 42)
  - `float`: Decimal numbers (e.g., 3.14)
  - `str`: Strings (e.g., "Hello")
  - `bool`: Boolean values (True or False)
  - `list`: Ordered collection (e.g., `[1, 2, 3]`)
  - `tuple`: Immutable ordered collection (e.g., `(4, 5, 6)`)
  - `dict`: Key-value pairs (e.g., `{"name": "Alice", "age": 25}`)
  - `set`: Unordered unique elements (e.g., `{10, 20, 30}`)

#### Fun Fact:
Python is **dynamically typed**, meaning you don’t have to declare the type of a variable when creating it.

### Exercise:
```python
x = 42
y = 3.14
z = 'Hello'
print(type(x), type(y), type(z))
```

---

## 2.3. Operators and Operands
### Research:
- **Arithmetic operators**: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- **Comparison operators**: `==`, `!=`, `>`, `<`, `>=`, `<=`
- **Logical operators**: `and`, `or`, `not`

#### Fun Fact:
Python uses `//` for **floor division**, ensuring the result is always an integer.

### Exercise:
```python
a = 10
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

print("Greater:", a > b)
print("Smaller:", a < b)
print("Equal:", a == b)
print("Not Equal:", a != b)
print("AND:", True and False)
print("OR:", True or False)
```

---

## 2.4. Function Calls
### Fun Fact:
Python treats **functions as first-class objects**, meaning they can be assigned to variables and passed as arguments.

### Exercise:
```python
numbers = [5, 3, 8, 1]
print("Max - Min:", max(numbers) - min(numbers))
```

```python
greet = print
greet("Hello, World!")
```

---

## 2.5. Data Types
### Research:
Python is **dynamically typed**, meaning variable types are determined at runtime.

### Exercise:
```python
a = 10
b = "Python"
c = 3.14
print(type(a), type(b), type(c))
```

---

## 2.6. Type Conversion Functions
### Fun Fact:
Python provides built-in functions like `int()`, `float()`, and `str()` for type conversions.

### Exercise:
```python
num = "123"
converted_num = int(num)
print(converted_num, type(converted_num))
```

---

## 2.7. Variables
### Research:
Python variables are **references** to memory locations where data is stored.

### Exercise:
```python
x = 5
print("Initial x:", x)

x = "Hello"
print("Reassigned x:", x)
```

---

## 2.8. Variable Names and Keywords
### Exercise:
Try using reserved keywords as variable names and observe the errors:
```python
import keyword
print(keyword.kwlist)
```

#### Fun Fact:
Using meaningful names like `total_price` is better than `tp` because it improves code readability.

---

## 2.10. Statem