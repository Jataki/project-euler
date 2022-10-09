import time
# import math

# Timer start
start_time = time.perf_counter()

# Code goes here
# Using a sieve
# Sieve of Eratosthenes with odds only
sieve = [True] * 2000000
sum = 2
for i in range(3, 2000000, 2):
  if sieve[i] == True:
    sum += i
    for j in range(i**2, 2000000, i):
      sieve[j] = False
print(sum)

# Brute force
# def is_prime(number: int):
#   if number == 1:
#     return True
#   for i in range(2, int(math.sqrt(number))+1):
#     if number % i == 0:
#       return False
#   return True

# prime_sum = 2
# i = 3
# while i < 2000000:
#   if(is_prime(i)):
#     prime_sum += i
#   i += 2
# print(prime_sum)

# Timer finish
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"The execution time is: {execution_time} seconds")