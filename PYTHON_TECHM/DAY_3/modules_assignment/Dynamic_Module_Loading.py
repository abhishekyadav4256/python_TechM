import importlib

def dynamic_import_and_execute(module_name, function_name, argument):
    try:
        module = importlib.import_module(module_name)  # Dynamically import the module
        func = getattr(module, function_name)  # Get the function reference
        result = func(argument)  # Execute the function with the provided argument
        print(f"Output: {result}")
    except (ModuleNotFoundError, AttributeError, TypeError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    module_name = input("Enter module name: ")
    function_name = input("Enter function name: ")
    argument = float(input("Enter argument: "))  # Assuming numeric input for simplicity
    dynamic_import_and_execute(module_name, function_name, argument)