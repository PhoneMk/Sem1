import csv
def load_books_from_csv(filename, books):
    try:
        filehandle = open(filename, 'r', encoding='utf-8-sig') 
        book_list = csv.DictReader(filehandle)
        for row in book_list:
            books.append({
                'bookID': row['bookID'],
                'title': row['title'],
                'authors': row['authors'],
                'average_rating': row['average_rating'],
                'isbn': row['isbn'],
                'isbn13': row['isbn13'],
                'language_code': row['language_code'],
                'num_pages': row['num_pages'], 
                'ratings_count': row['ratings_count'],
                'text_reviews_count': row['text_reviews_count'],
                'publication_date': row['publication_date'],
                'publisher': row['publisher']
                })
        print(f'Books loaded from {filename}')
    except FileNotFoundError:
        print(f'Error: File "{filename}" not found')

def save_books_to_csv(filename, books):
    filehandle = open(filename, 'w', newline='', encoding='utf-8-sig')
    fieldnames = books[0].keys()
    writer = csv.DictWriter(filehandle, fieldnames=fieldnames)
    writer.writeheader()
    for book in books:
        writer.writerow(book)
    print(f'Books saved to {filename}')

def list_all_books(books):
    for book in books:
        print(f"{book['bookID']}\t{book['title']}\t{book['authors']}\t{book['average_rating']}\t{book['language_code']}\t"
              f"{book['num_pages']}\t{book['publication_date']}\t{book['publisher']}")

def show_book_information(book_id, books):
    for book in books:
        if str(book['bookID']) == str(book_id) or str(book['isbn13']) == str(book_id):
            print("\nBook Information:")
            for key, value in book.items():
                print(f"{key.capitalize()}: {value}")
            return
    print(f"Error: Book with ID {book_id} not found in the collection")

books = []
while True:
    print("\nMenu:")
    print("Load, Save and List books from CSV file (1/2/3)")
    print("Show information of a book (4)")
    print("Exit (5)")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        filename = input("Enter CSV filename to load books from: ")
        load_books_from_csv(filename, books)
    elif choice == '2':
        filename = input("Enter CSV filename to save books to: ")
        save_books_to_csv(filename, books)
    elif choice == '3':
        list_all_books(books)
    elif choice == '4':
        book_id = input("Enter book ID to show information: ")
        show_book_information(book_id, books)
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")