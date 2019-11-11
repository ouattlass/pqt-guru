#  Copyright (c) 2019.
#  @Author : Lassina OUATTARA
#  @Python code


book_list = []
number_of_iteration = 0
author_book_count = 0
author_books = []

# user providing the number of book
number_of_book = int(input('\nEnter the number of book: '))

# iteration to create books
while number_of_iteration < number_of_book:

    # Filling the book information and adding book to the book_list
    print(F'\nBook {number_of_iteration+1} information...')
    book_object = {'name': input('enter the book name: '), 'author': input('enter the Author name: '),
                   'price': input('enter the book price: '), 'isbn': input('enter the ISBN: ')}
    book_list.append(book_object)

    number_of_iteration += 1


# getting user input (author name)
author_name = input('\nEnter Author Name to find all books written by that Author: ')

# iteration to find the book related to the author,if book author found with the same author,add it to
# the author_books
for book in book_list:
    if author_name == book['author']:
        author_book_count += 1
        author_books.append(book)

# printing the contain of author_books
print(F'{author_book_count} Book(s) found for Author {author_name} :)\n')
book_index = 0
for book in author_books:
    book_index += 1
    print('*' * 15)
    print(F'Book number: {book_index}')
    print(F"Name:{book['name']}\n"
          F"Author:{book['author']}\n"
          F"Price:{book['price']}\n"
          F"ISBN:{book['isbn']}")
    print('*' * 15, '\n')
