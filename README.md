# Project Euler

This repository contains all personal solutions regarding Project Euler problems. All of these are written in Python3.

## What is Project Euler?

Project Euler is a series of challenging mathematical/computer programming problems that will require more than just mathematical insights to solve. [Learn more](https://projecteuler.net/about)

## Code of Ethics

None of the solutions have been copied nor will they ever be. Every coded solution presented here is of my own design. Directly searching for the solution or any other form of finding the answer is prohibited. One can look for algorithms (no need to reinvent the wheel) - if you need an algorithm to efficiently find primes, for example, you can look for pseudo-code solutions that fit the intended solution; but implementation is always to the coder.

## Running a solution

Considering `<# problem>` is always a three digit number representing the problem you'd like to get the answer to, running a solution is a simple matter of running the command:

`python /path/to/repo/<# problem>/main.py`

E.g.: if I want to access the answer for problem 15, I'd run `python /home/jataki/project-euler/015/main.py`

All files are ready to provide the answer in the console, as well as a timer showing how long the solution took to run, in seconds.

## Reading the code

Code structure is always the same:

1. Imports
2. Timer start
3. Solution code
    a. This can have multiple solutions commented, leaving out only the best one (time and memory wise)
4. Timer finish
