# module_a.py

def func_a():
    return "Function A"

def call_func_b():
    from module_b import func_b  # Lazy import to avoid circular dependency
    return func_b()

if __name__ == "__main__":
    print(call_func_b())
    
