import math
import time

# Timer start
start_time = time.perf_counter()

# Code goes here
# c = 1000 - a - b = sqrt(a²+b²)
found_c = False
for a in range(0, 400):
  for b in range(0, 400):
    if 1000 - a - b == math.sqrt(a**2 + b**2):
      print(a*b*(1000-a-b))
      found_c = True
      break
  if found_c: break    

# Timer finish
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"The execution time is: {execution_time} seconds")