x = list(range(5))
print(x)
def delete_books(books):
    # Display options for deletion filters
    print("\nChoose a filter for deletion:")
    print("1. Delete by bookID")
    print("2. Delete by isbn13")
    print("3. Delete by average_ratings")
    print("4. Delete by language_code")
    print("5. Delete by publication_date")
    print("6. Delete by publisher")
    
    # Get user choice
    choice = input("Enter your choice (1-6): ")

    # Process user's choice
    if choice == '1':
        # Delete by bookID
        book_id_to_delete = input("Enter the bookID to delete: ")
        books = [book for book in books if book['bookID'] != book_id_to_delete]
    elif choice == '2':
        # Delete by isbn13
        isbn13_to_delete = input("Enter the isbn13 to delete: ")
        books = [book for book in books if book['isbn13'] != isbn13_to_delete]
    elif choice == '3':
        # Delete by average_ratings
        ratings_filter = input("Enter 'greater' or 'less' to delete books with greater or less average_ratings: ")
        threshold_ratings = float(input("Enter the threshold average_ratings: "))
        if ratings_filter == 'greater':
            books = [book for book in books if float(book['average_rating']) <= threshold_ratings]
        elif ratings_filter == 'less':
            books = [book for book in books if float(book['average_rating']) >= threshold_ratings]
    elif choice == '4':
        # Delete by language_code
        language_code_to_delete = input("Enter the language_code to delete: ")
        books = [book for book in books if book['language_code'] != language_code_to_delete]
    elif choice == '5':
        # Delete by publication_date
        publication_date_to_delete = input("Enter the publication_date to delete: ")
        books = [book for book in books if book['publication_date'] != publication_date_to_delete]
    elif choice == '6':
        # Delete by publisher
        publisher_to_delete = input("Enter the publisher to delete: ")
        books = [book for book in books if book['publisher'] != publisher_to_delete]
    else:
        # Invalid choice
        print("Invalid choice. Please enter a number between 1 and 6.")

    # Print result
    print("Books deleted successfully.")
    return books

# Example usage:
# books = delete_books(books)
if choice == '1':
    # User chose to delete by bookID
    book_id_to_delete = input("Enter the bookID to delete: ")

    # Create a new list to store books that are not to be deleted
    updated_books = []

    # Iterate through each book in the original list
    for book in books:
        # Check if the book's bookID is not equal to the one to be deleted
        if book['bookID'] != book_id_to_delete:
            # If not equal, add the book to the updated list
            updated_books.append(book)

    # Update the books list with the updated list
    books = updated_books




def sort_books(books, sort_key, ascending=True):
    """
    Sort the books based on the specified key in ascending or descending order.

    Parameters:
    - books: List of dictionaries representing books.
    - sort_key: Key based on which the books should be sorted.
    - ascending: True for ascending order, False for descending order.

    Returns:
    - List of sorted books.
    """
    reverse_order = not ascending

    if sort_key == 'bookID':
        sorted_books = sorted(books, key=lambda x: int(x['bookID']), reverse=reverse_order)
    elif sort_key == 'title':
        sorted_books = sorted(books, key=lambda x: x['title'], reverse=reverse_order)
    elif sort_key == 'average_rating':
        sorted_books = sorted(books, key=lambda x: float(x['average_rating']), reverse=reverse_order)
    elif sort_key == 'num_pages':
        sorted_books = sorted(books, key=lambda x: int(x['num_pages']), reverse=reverse_order)
    elif sort_key == 'publication_date':
        sorted_books = sorted(books, key=lambda x: x['publication_date'], reverse=reverse_order)
    else:
        print("Invalid sort key. Please choose from: bookID, title, average_rating, num_pages, publication_date")
        return books

    return sorted_books

sorted_books = sort_books(books, 'average_rating', ascending=False)
list_all_books(sorted_books)


def sort_books(books):
    print("\nChoose a key to sort by:")
    print("1. bookID")
    print("2. title")
    print("3. average_ratings")
    print("4. num_pages")
    print("5. publication_date")

    choice = input("Enter your choice (1-5): ")
    order_choice = input("Sort in ascending (a) or descending (d) order? ").lower()

    if choice == '1':
        sort_key = 'bookID'
    elif choice == '2':
        sort_key = 'title'
    elif choice == '3':
        sort_key = 'average_rating'
    elif choice == '4':
        sort_key = 'num_pages'
    elif choice == '5':
        sort_key = 'publication_date'
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
        return

    sorted_books = sort_books_by_key(books, sort_key, order_choice)
    list_all_books(sorted_books)


def sort_books_by_key(books, sort_key, order_choice):
    # Define a lambda function to extract the specified key from a book
    

    # Determine whether to sort in ascending or descending order
    reverse_order = order_choice == 'd'

    # Use the sorted function with the custom key function and reverse parameter
    if sort_key == 'bookID':
        sorted_books = sorted(books, key=lambda x: int(x['bookID']), reverse=reverse_order)
    elif sort_key == 'title':
        sorted_books = sorted(books, key=lambda x: x['title'], reverse=reverse_order)
    elif sort_key == 'average_rating':
        sorted_books = sorted(books, key=lambda x: float(x['average_rating']), reverse=reverse_order)
    elif sort_key == 'num_pages':
        sorted_books = sorted(books, key=lambda x: int(x['num_pages']), reverse=reverse_order)
    elif sort_key == 'publication_date':
        sorted_books = sorted(books, key=lambda x: x['publication_date'], reverse=reverse_order)
    return sorted_books
