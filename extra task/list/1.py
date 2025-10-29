""" list is mutable orederedseuensbale indexable collection datatype 
but its allow duplicate 
its store similiar and dis -similiar datattype data

Create a list of 10 numbers and print it.

Access first, middle, and last elements of a list.

Find the length of a list without using len().

Add an element at the end of a list using append().

Insert an element at a specific position.

Remove an element by value using remove().

Delete an element by index using del.

Sort a list in ascending and descending order.

Reverse a list using slicing.

Count how many times a value appears in the list.

Find the maximum, minimum, and sum of list elements.

Take 5 numbers from user input and store them in a list.

Check if an element exists in the list.

Copy a list using slicing and using copy().

Convert a string into a list of words using s
"""

# nt at a specific position.

list1=[1,2,3,4,2,2,2,6,32,2]
element=int(input("Enter Element = "))
index=int(input("enter position= "))
list1.insert(index,element)
print(list1)