# Advanced Import Strategies
import importlib
def safe_import_and_execute(module_name, function_name, *args):
    try:
        module = importlib.import_module(module_name)  # Dynamically import the module
        if hasattr(module, function_name):  # Check if function exists
            func = getattr(module, function_name)
            result = func(*args)  # Execute function with arguments
            print(f"Output: {result}")
        else:
            print(f"Error: Function '{function_name}' not found in module '{module_name}'.")
    except ModuleNotFoundError:
        print(f"Error: Module '{module_name}' not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    module_name = input("Enter module name: ")
    function_name = input("Enter function name: ")
    args = input("Enter arguments (comma-separated): ").split(',')
    args = [float(arg) if arg.replace('.', '', 1).isdigit() else arg for arg in args]  # Convert numeric inputs
    safe_import_and_execute(module_name, function_name, *args)
