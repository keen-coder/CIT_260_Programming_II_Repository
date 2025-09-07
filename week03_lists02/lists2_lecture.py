list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [item**2 for item in list1]
print(list2)

animals = ['dog', 'cat', 'chicken', 'fish', 'seal', 'horse']
str_lens = [len(a) for a in animals]
print(str_lens)

list1 = [56, 2, 3, 79, 100, 12, 43, 42, 10]
list2 = [x for x in list1 if x >= 20]
print(list2)

animals = ['dog', 'cat', 'chicken', 'fish', 'seal', 'horse']
result = [a for a in animals if len(a) >= 4]
print(result)