# module_b.py

def func_b():
    return "Function B"

def call_func_a():
    from module_a import func_a  # Lazy import to avoid circular dependency
    return func_a()
    

if __name__ == "__main__":
    print(call_func_a())