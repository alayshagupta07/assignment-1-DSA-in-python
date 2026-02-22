#unit 1 assignment DSA 
# Name - Alaysha Gupta 
# Roll No.- 2501010113
# Subject - Data Structures 
# Class - BTECH CSE CORE SECTION A 
# TASK TO DO 

"""1.Recursive factorial and recursive Fibonacci (naive + memoized recommended)
   2.Time & space complexity for both, with clear justification (why Fibonacci naive is
     inefficient)
   3. Tower of Hanoi recursion + trace for N=3 + time complexity
   4.Recursive binary search + recurrence-based complexity explanation"""

#1.recursive function to compute factorial of a number and analyze its time and space complexity.
"""Factorial is defined as:
        n!=n*(n-1)!
        Base Case: 0! = 1"""
# Recursive Factorial

def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    
    # Recursive case
    return n * factorial(n - 1)

# Example
print("Factorial of 5 is:", factorial(5))

#Explanation
"""If n is 0 or 1 → return 1
Otherwise → multiply n with factorial(n-1)
Function keeps calling itself until base case is reached"""

"""Time Complexity:-
Each call reduces n by 1.
recurrence :-
Recurrence:
T(n) = T(n-1) + O(1)
solving:-
T(n)= O(n)
Space Complexity:-
Maximum recursion depth = O(n)"""

#Recursive Fibonacci
"""Fibonacci is defined as:-
F(n)=F(n−1)+F(n−2)
Base cases:
F(0)=0 , F(1)=1"""

#Naive Recursive Fibonacci 

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print("Fibonacci of 6 is:", fib(6))

#Explanation 
"""Function calls itself twice
Same values are computed repeatedly

Example: fib(3) gets calculated multiple times"""

""" Time Complexity :-
This grows exponentially:-
Recurrence:
T(n) = T(n-1) + T(n-2) + O(1)

T(n) = O(2^n)

Reason for inefficiency:
Because of repeated recursive calls.

Space Complexity

Maximum recursion depth = n
         O(n)"""

# Memoized Fibonacci
def fib_memo(n, memo=None):
    if memo is None:
        memo = {}

    # Check if value already computed
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

print("Fibonacci of 6 (memoized) is:", fib_memo(6))

"""Explanation
Each Fibonacci number calculated only once
Avoids repeated work"""

"""
Time Complexity: Each value computed once:O(n)
Space Complexity:O(n)"""

#Tower Of Hanoi 
"""Move only one disk at a time
   Larger disk cannot be placed on smaller disk"""

def hanoi(n, source, auxiliary, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return
    
    hanoi(n-1, source, destination, auxiliary)
    print("Move disk", n, "from", source, "to", destination)
    hanoi(n-1, auxiliary, source, destination)

# Example
hanoi(3, 'A', 'B', 'C')
"""Trace for N=3:

1. Move disk 1 from A → C
2. Move disk 2 from A → B
3. Move disk 1 from C → B
4. Move disk 3 from A → C
5. Move disk 1 from B → A
6. Move disk 2 from B → C
7. Move disk 1 from A → C

Total moves = 2^3 - 1 = 7"""

#Time Complexity : O(2^n)
#Space Complexity: O(n)

"""Recursive Binary Search
 Problem Statement:-
 Search a target element in a sorted array using recursion."""

# Recursive Binary Search

def binary_search(arr, left, right, target):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, left, mid-1, target)
    else:
        return binary_search(arr, mid+1, right, target)

# Example
arr = [2, 4, 6, 8, 10, 12]
print("Element found at index:", binary_search(arr, 0, len(arr)-1, 8))

""" Time Complexity
Recurrence:
T(n) = T(n/2) + O(1)

T(n) = O(log n)

 Space Complexity : O(logn)"""








