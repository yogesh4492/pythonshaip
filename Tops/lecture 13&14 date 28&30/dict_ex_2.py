book={
    "name":"Python Programming",
    "author":'monty',
    "price":149.67

}

print(book)

# print(book[0])


print(book['name'])
print(book['price'])
# print(book['year':2025]) 

print(book.get('name'))
print(book.get('price'))
print(book.get('year')) #its give none but not throw error