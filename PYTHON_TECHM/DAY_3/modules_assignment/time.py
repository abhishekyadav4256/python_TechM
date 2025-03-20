import time

# Measure import time for single import
start = time.time()
import math
end = time.time()
print(f"Single import time: {end - start:.6f} seconds")

# Measure import time for importing everything from a module
start = time.time()
from math import *
end = time.time()
print(f"Import everything time: {end - start:.6f} seconds")
