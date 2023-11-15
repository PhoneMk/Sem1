import csv
def load_books(filename, books):
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
    print("Book ID\tTitle\tAuthors\tAverage Rating\tLanguage Code\tNum Pages\tPublication Date\tPublisher")
    for book in books:
        print(f"{book['bookID']}\t{book['title']}\t{book['authors']}\t{book['average_rating']}\t{book['language_code']}\t"
              f"{book['num_pages']}\t{book['publication_date']}\t{book['publisher']}")

def show_book_info(book_id, books):
    for book in books:
        if str(book['bookID']) == str(book_id) or str(book['isbn13']) == str(book_id):
            print("\nBook Information:")
            for key, value in book.items():
                print(f"{key.capitalize()}: {value}")
            return
    print(f"Error: Book with ID {book_id} not found in the collection")

def insert_book(books):
    new_book = {
        'bookID': input("Enter Book ID: "),
        'title': input("Enter Title: "),
        'authors': input("Enter Authors: "),
        'average_rating': input("Enter Average Rating: "),
        'isbn': input("Enter ISBN: "),
        'isbn13': input("Enter ISBN13: "),
        'language_code': input("Enter Language Code: "),
        'num_pages': input("Enter Number of Pages: "),
        'ratings_count': input("Enter Ratings Count: "),
        'text_reviews_count': input("Enter Text Reviews Count: "),
        'publication_date': input("Enter Publication Date (MM/DD/YYYY): "),
        'publisher': input("Enter Publisher: ")
    }
    duplicate = False
    for book in books:
        if book['isbn13'] == new_book['isbn13'] or book['bookID'] == new_book['bookID']:
            duplicate = True
        break
    if duplicate:
        print("Error: Book with the same ID already exists.")
    else:
        books.append(new_book)
        print("Book successfully inserted.")
    return books 

def search_books(books, keyword):
    result = []
    keyword = keyword.lower()
    for book in books:
        title = book['title'].lower()
        authors = book['authors'].lower()
        if keyword in title or keyword in authors:
            result.append(book)
    return result

def view_statistics(books):
    # the number of books
    num_books = len(books)
    # the number of distinct authors
    distinct_authors = set()
    for book in books:
        authors = book['authors'].split('/') 
        distinct_authors.update(authors)
    num_distinct_authors = len(distinct_authors)
    # Calculate the total number of pages
    total_pages = 0
    for book in books:
        total_pages += int(book['num_pages'])
    # number of distinct publishers
    distinct_publishers = set()
    for book in books:
        distinct_publishers.add(book['publisher'])
    num_distinct_publishers = len(distinct_publishers)
    #number of pages per book
    if num_books == 0:
        return 0
    average_pages_per_book = total_pages / num_books 
    #books per year
    years = set()
    total_books = 0
    for book in books:
        publication_year = int(book['publication_date'].split('/')[-1])
        years.add(publication_year)
        total_books += 1
    total_years = len(years)
    if total_years == 0:
        return 0  
    avg_books = total_books / total_years
    
    print("\nStatistical Information:")
    print("Number of Books:", num_books)
    print("Number of Distinct Authors:", num_distinct_authors)
    print("Total Number of Pages:", total_pages)
    print("Number of Distinct Publishers:", num_distinct_publishers)
    print(f"Average Number of Pages per Book: {average_pages_per_book:.2f}")
    print(f"Average number of books per year: {avg_books:.2f}")

books = []
while True:
    print("\nMenu:")
    print("Load, Save and List books from CSV file (1/2/3)")
    print("Show information or Statistics of a book (4,5)")
    print("Search from CSV (6)")
    print("Exit (7)")
    num = input("Enter your choice (1-7): ")

    if num == '1':
        filename = input("Enter CSV filename to load books from: ")
        load_books(filename, books)
    elif num == '2':
        filename = input("Enter CSV filename to save books to: ")
        save_books_to_csv(filename, books)
    elif num == '3':
        list_all_books(books)
    elif num == '4':
        book_id = input("Enter book ID to show information: ")
        show_book_info(book_id, books)
    elif num == '5':
        view_statistics(books)
    elif num == '6':
        keyword = input("Enter keyword to search for books: ")
        result = search_books(books, keyword)
        if result:
            print("\nMatching Books:")
            for book in result:
                print(f"{book['bookID']}\t{book['title']}\t{book['authors']}")
        else:
            print("No matching books found.")
    elif num == '7':
        insert_book(books)
    elif num == '8':
        print("Exit the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")