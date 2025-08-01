# Python List Methods with Results Stored in Variables

# Original List
fruits = ['apple', 'banana','orange']
list1 = fruits.copy()  # To keep original
extend = ['orange', 'grape']
# 1. append() – Add one item
list_append = list1.copy()
list_append.append('cherry')

# 2. extend() – Add multiple items
list_extend = list1.copy()
list_extend.extend(extend)

# 3. insert() – Insert at specific index
list_insert = list1.copy()
list_insert.insert(1, 'kiwi')

# 4. remove() – Remove an item
list_remove = ['apple', 'banana', 'cherry']
list_remove.remove('banana')

# 5. pop() – Remove and return last item
list_pop = ['apple', 'banana', 'cherry']
popped_item = list_pop.pop()  # Will remove 'cherry'

# 6. clear() – Clear all elements
list_clear = list1.copy()
list_clear.clear()

# 7. index() – Get index of an item
list_index = ['apple', 'banana', 'cherry']
index_of_cherry = list_index.index('cherry')

# 8. count() – Count occurrences
list_count = ['apple', 'banana', 'apple', 'cherry']
count_apple = list_count.count('apple')

# 9. sort() – Sort list
list_sort = [5, 3, 9, 1]
list_sort.sort()  # Sort in-place
sorted_list = list_sort.copy()

# 10. reverse() – Reverse list
list_reverse = [1, 2, 3, 4]
list_reverse.reverse()
reversed_list = list_reverse.copy()

# 11. copy() – Duplicate list
list_copy_original = ['a', 'b', 'c']
list_copied = list_copy_original.copy()

# Print Results
print("1. append():", list_append)
print("2. extend():", list_extend)
print("3. insert():", list_insert)
print("4. remove():", list_remove)
print("5. pop():", list_pop, "| Popped item:", popped_item)
print("6. clear():", list_clear)
print("7. index(): Index of 'cherry' is", index_of_cherry)
print("8. count(): 'apple' occurs", count_apple, "times")
print("9. sort():", sorted_list)
print("10. reverse():", reversed_list)
print("11. copy():", list_copied)

a = 6
b = 5
c=a
a=b
b=c

a,b = b,a
print(a,b)