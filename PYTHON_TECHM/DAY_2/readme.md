# Advanced Debugging: Notes and Assignment

## 3.1. Introduction to Debugging
### 3.1.1. Learning Goals
By the end of this module, students should be able to:
- Understand the significance of debugging in the software development lifecycle.
- Identify common types of programming errors.
- Apply various debugging techniques to isolate and fix bugs.
- Utilize debugging tools effectively.

### 3.1.2. Objectives
- Grasp the real-world importance of debugging.
- Learn strategies to prevent bugs.
- Master the use of debugging tools and techniques.
- Practice advanced problem-solving skills.

## 3.2. Programming in the Real World
In real-world programming, code rarely works perfectly on the first try. Debugging is a critical skill that involves identifying and fixing errors in code. Professional developers spend a significant portion of their time debugging and ensuring code reliability. Understanding the art of debugging can make the difference between a novice and a proficient developer.

### Common Types of Errors:
- **Syntax Errors**: Mistakes in the code structure (e.g., missing colons, unmatched parentheses).
- **Runtime Errors**: Errors that occur while the program is running (e.g., division by zero).
- **Logic Errors**: The program runs without crashing but produces incorrect results.

### Debugging Process:
1. Reproduce the error.
2. Isolate the problematic code.
3. Fix the bug.
4. Test thoroughly to ensure the fix is correct and doesn’t introduce new issues.

### Additional Reading:
- [Python Official Debugging Guide](https://docs.python.org/3/library/pdb.html)
- [Real Python Debugging Tutorial](https://realpython.com/python-debugging-pdb/)
- [Effective Debugging Techniques](https://realpython.com/python-bug-hunting/)

## 3.3. Debugging
### 3.3.1. How to Avoid Debugging
While debugging is inevitable, writing clean and predictable code reduces the chances of bugs. Here are strategies to minimize bugs:
- **Write Clear Code**: Use meaningful variable names and write self-explanatory functions.
- **Test Incrementally**: Test your code step-by-step rather than writing everything at once.
- **Use Assertions**: Assertions help catch unexpected states early.
- **Version Control**: Commit working code often, so you can easily revert to a stable state.
- **Peer Reviews**: Having another person review your code can uncover issues you might have missed.

### Tools and Techniques:
- **Print Statements**: Insert print statements to trace variable values.
- **Debuggers**: Use tools like Python's built-in `pdb` or IDE-integrated debuggers.
- **Logging**: Implement logging to track the flow of execution and catch unexpected behaviors.
- **Rubber Duck Debugging**: Explain your code to someone (or an inanimate object) to uncover mistakes.

### Pro Tips:
- Break down problems into smaller chunks.
- Focus on one bug at a time.
- Write test cases for critical parts of your code.
- Avoid making multiple changes at once while debugging.

## Understanding Try-Except (Try-Catch)
The `try` and `except` blocks in Python help handle exceptions gracefully, ensuring the program doesn’t crash unexpectedly.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

### Steps to Use Try-Except:
1. Identify the code that might raise an exception.
2. Wrap the risky code inside a `try` block.
3. Use `except` to handle specific exceptions.
4. Optionally add `else` for code that runs if no exceptions occur and `finally` for cleanup actions.

### Learn More:
- [Python Exceptions Documentation](https://docs.python.org/3/tutorial/errors.html)
- [Real Python Try-Except Guide](https://realpython.com/python-exceptions/)

---

The following section contains practical assignments. See the accompanying Jupyter Notebook for solutions and implementation.
