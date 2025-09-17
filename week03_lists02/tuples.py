tuple1 = (1,)
print(type(tuple1))

print(help(tuple))

# A good use for tuples, is when you want to return multiple values
# from a function.
# You get an immutable sequence back from your function that you can be
# sure cannot be changed. You can always convert it to a list later if necessary

# find the min and max values of a given list
def min_max(values):
    return (min(values), max(values))  # tuple of results

nums = [10, 3, 7, 42, 5]
result = min_max(nums)
print(result)        # (3, 42)
low, high= result   # tuple unpacking
print(low, high)     # 3 42

# Tuples are great for coordinates
point = (10, 20)
print(f"x={point[0]}, y={point[1]}")

# Tuples are also good for storing record information like a row in a database
employee = ("Alice", "HR", 75000)
name, dept, salary = employee
print(f"{name} works in {dept} earning ${salary}")