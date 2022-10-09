import time

# Timer start
start_time = time.perf_counter()

# Code goes here
def is_palindrome_legacy(number: int):
  as_str = str(number)
  return all(as_str[i] == as_str[len(as_str) - 1 - i] for i in range(0, round(len(as_str) / 2)))

def is_palindrome(number: int):
  s = str(number)
  return s == s[::-1]

r = 0
for i in range(999, 450, -1):
  for j in range(999, 450, -1):
    p = i * j
    if is_palindrome(p):
      r = p if p > r else r
      break
print(r)

# Timer finish
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"The execution time is: {execution_time} seconds")