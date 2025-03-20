# test_import.py

import side_effect_module  # This will immediately trigger the print statement from the module

print("Module imported successfully.")
print(side_effect_module.greet())  # Calling a function from the module
