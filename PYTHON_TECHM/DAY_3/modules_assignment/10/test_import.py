import sys
import mymodule  # This will print "Module mymodule has been imported!" on the first import

# Check if 'mymodule' exists in the import cache
print("Checking import cache:")
print(sys.modules['mymodule'])

# Modifying 'mymodule.py' won't reflect in this script unless we reload it
import importlib

# Reload the module
importlib.reload(mymodule)

print("After reload:")
print(mymodule.greet())  # This will reflect the latest version of the module if it was modified
  