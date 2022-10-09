import time
import math

# Timer start
start_time = time.perf_counter()

# Code goes here

# Using a sieve
# Sieve of Eratosthenes with odds only
odds = [i for i in range(3, 150000, 2)]
sieve = [True] * 150000
counter = 1
for i in odds:
  if sieve[i] == True:
    counter += 1
    if counter == 10001:
      print(i)
      break
    for j in range(i**2, 150000, i):
      sieve[j] = False

# Using brute force
# def is_prime(number: int):
#   if number == 1:
#     return True
#   for i in range(2, int(math.sqrt(number))+1):
#     if number % i == 0:
#       return False
#   return True

# # BF Solution 1
# # Using an array
# all_primes = []
# i = 3
# while len(all_primes) < 10000:
#   if(is_prime(i)):
#     all_primes.append(i)
#   i += 2
# print(all_primes[9999])

# # BF Solution 2
# # Using a counter
# i = 3
# prime_counter = 1
# while True:
#   if(is_prime(i)):
#     prime_counter += 1
#   if prime_counter == 10001:
#     print(i)
#     break
#   i += 2


# Timer finish
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"The execution time is: {execution_time} seconds")