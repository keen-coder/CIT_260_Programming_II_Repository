import time # Module that can be used to record a rough runtime of a function

""" 
This example shows up to improve the efficiency of the fibonacci recursion problem 
using a technique called memoization.

Memoization is a programming technique used to optimize performance by storing the 
results of expensive function calls and returning the cached result when the same 
inputs occur again. It's especially useful in recursive algorithms or functions with 
overlapping subproblems.
"""

FIB_INDEX = 500


def main():
    # time slow_fib
    # start = time.time()
    # result = slow_fib(FIB_INDEX)
    # end = time.time()

    # print('\nslow_fib Results: ')
    # print(f'\tValue:\t{result}')
    # print(f'\tExecution Time:\t{end - start:.6f} seconds')

    #time fast_fib
    start = time.time()
    result = fast_fib(FIB_INDEX)
    end = time.time()

    print('\nfast_fib Results: ')
    print(f'\tValue:\t{result}')
    print(f'\tExecution Time:\t{end - start:.6f} seconds')


def fast_fib(index: int) -> int:

    # Initialize the cache with the first two index values.
    # Index is the key, value is the fib value at that index.
    cache: dict[int:int] = {0:0, 1:1}

    # Recursive helper function
    def fast_fib(index, cache):
        if index in cache:
            return cache[index]
        else:
            # Store the new computed index value in the cache
            cache[index] = fast_fib(index - 1, cache) + fast_fib(index - 2, cache)
            return cache[index]
        
    return fast_fib(index, cache)
        
# Example of binary recursion, two recursive branches always called
def slow_fib(index: int) -> int:
    #print(f'computing fib({index})')

    if index == 0:      # Base Case 1
        return 0
    elif index == 1:    # Base Case 2
        return 1
    else:               # Recursive Case
        return slow_fib(index - 1) + slow_fib(index - 2)


if __name__ == '__main__':
    main()