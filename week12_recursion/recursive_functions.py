
def main():
    print(f'5!\t=\t{factorial(5)}')
    print(f'20!\t=\t{factorial(20)}')

    print(f'fibonacci(50)\t=\t{fibonacci_slow(50)}')
    print(f'fibonacci(7)\t=\t{fibonacci_slow(7)}')

    print(f'2^5\t=\t{power(2, 5)}')
    print(f'7^9\t=\t{power(7, 9)}')
    
    print_list([1, 2, 3, 4, 5])
    print()
   
    print(f'palindrome("noon")\t=\t{palindrome('noon')}')
    print(f'palindrome("noon")\t=\t{palindrome('moon')}')

    data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(f'binary_search(10)\t=\t{binary_search(data, 7)}')
    print(f'binary_search(10)\t=\t{binary_search(data, 90)}')


    reverse_list(data, 0, len(data) - 1)
    print(data)


    table = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
    
    print_2D_list(table)
    print('function finished')

    print(sum(10))
    print(sum(11))

# sum all even values from 2 to n


# sum(16)
# sum(17)
# sum(100)

def sum(n):
    if n % 2 != 0:
        return sum(n-1)
    elif n == 2:
        return 2
    else:
        return n + sum(n - 2)

# Search
def binary_search(data: list[int], key: int):
    # Recursive Helper Method
    def binary_search(data: list[int], key: int, low: int, high: int) -> int:
        mid: int = (low + high) // 2
        
        if low > high:          # Base Case 1
            return -1
        elif key == data[mid]:    # Base Case 2
            return mid
        if key < data[mid]:     # Recursive Case 1
            return binary_search(data, key, low, mid - 1)
        else:
            return binary_search(data, key, mid + 1, high)

    return binary_search(data, key, 0, len(data) - 1)

def factorial(n: int) -> int:
    if (n == 0 or n == 1):  # Base case !0 or !1 are both 1
        return 1
    else:                   # Recursive case
        return n * factorial(n - 1) 


# Example of binary recursion, two recursive branches always called
def fibonacci_slow(index: int) -> int:
    #print(f'computing fib({index})')

    if index == 0:      # Base Case 1
        return 0
    elif index == 1:    # Base Case 2
        return 1
    else:               # Recursive Case
        return fibonacci_slow(index - 1) + fibonacci_slow(index - 2)


def palindrome(s: str) -> bool:
	
	# Recursive helper function
    def palindrome(s: str, low: int, high: int) -> bool:
        if low >= high:         # Base Case 1
            return True
        elif s[low] != s[high]: # Base Case 2
            return False
        else:
            return palindrome(s, low + 1, high - 1)
		
    return palindrome(s, 0, len(s) - 1)


def power(x: int, n: int) -> int:
    if n == 0:          # Base Case
        return 1
    else:               # Recursive Case
        return x * power(x, n - 1)


def print_list(data: list) -> None:
    # Recursive helper function
    # allows you to add more parameters as needed for the recursion, but allow
    # the top level function to be more simplified
    def print_list(data: list, index: int) -> None:
        # Hidden base case
        if index < len(data):
            print(str(data[index]), end=' ')
            print_list(data, index+1)

    print_list(data, 0)

















def print_2D_list(data: list[list]) -> None:
    # Recursive Helper Function
    def print_2D_list(data: list[list], 
                      row_num: int, col_num: int) -> None:
        if row_num >= len(data):    # Base Case
            return
        elif col_num >= len(data[row_num]):
            print()
            print_2D_list(data, row_num + 1, 0)
        else:
            print(data[row_num][col_num], end= ' ')
            print_2D_list(data, row_num, col_num + 1)
        
        
        # elif col_num >= len(data[row_num]): # Recursive Case 1
        #     print()
        #     print_2D_list(data, row_num + 1, 0)
        # else:
        #     print(data[row_num][col_num], end= ' ') # Recursive Case 2
        #     print_2D_list(data, row_num, col_num + 1)

    print_2D_list(data, 0, 0)

# No Helper function
def reverse_list(data: list, low: int, high: int):
    if low >= high:
        return
    else:
        temp = data[low]
        data[low] = data[high]
        data[high] = temp
        reverse_list(data, low + 1, high - 1)










if __name__ == '__main__':
    main()